import logging
import threading
from collections import Counter, defaultdict
from typing import Any

from ultralytics import YOLO

from app.common.exceptions import ConflictException, ServiceUnavailableException
from app.core.config import settings
from app.integrations.vision.base import ImageAnalysisRequest, ImageAnalysisResult

logger = logging.getLogger(__name__)


class UltralyticsYoloVisionProvider:
    provider_name = "ultralytics_yolo"

    _model_cache: dict[tuple[str, str], YOLO] = {}
    _model_cache_lock = threading.Lock()

    def __init__(self) -> None:
        self.model_name = settings.ultralytics_yolo_model
        self.device = settings.ultralytics_yolo_device
        self.confidence_threshold = settings.ultralytics_yolo_confidence_threshold
        self.iou_threshold = settings.ultralytics_yolo_iou_threshold
        self.image_size = settings.ultralytics_yolo_image_size
        self.max_detections = settings.ultralytics_yolo_max_detections

    def analyze_image(
        self,
        request: ImageAnalysisRequest,
    ) -> ImageAnalysisResult:
        source = self._resolve_source(request)

        try:
            model = self._get_or_create_model()

            predict_kwargs: dict[str, Any] = {
                "source": source,
                "conf": self.confidence_threshold,
                "iou": self.iou_threshold,
                "imgsz": self.image_size,
                "max_det": self.max_detections,
                "verbose": False,
                "stream": False,
            }

            if self.device:
                predict_kwargs["device"] = self.device

            results = model.predict(**predict_kwargs)

            if not results:
                return ImageAnalysisResult(
                    labels=[],
                    detections=[],
                    summary=(
                        "No se generaron resultados de visión para la imagen. "
                        "Se recomienda revisión manual."
                    ),
                    raw_response={
                        "provider": self.provider_name,
                        "model_name": self.model_name,
                        "source_kind": "url" if request.source_url else "local_file",
                    },
                )

            result = results[0]
            detections = self._extract_detections(result)
            labels = self._extract_labels(detections)
            summary = self._build_summary(labels, detections)

            return ImageAnalysisResult(
                labels=labels,
                detections=detections,
                summary=summary,
                raw_response={
                    "provider": self.provider_name,
                    "model_name": self.model_name,
                    "source_kind": "url" if request.source_url else "local_file",
                    "detection_count": len(detections),
                    "possible_incident_hint": self._infer_possible_incident_hint(labels, detections),
                    "original_image_shape": getattr(result, "orig_shape", None),
                },
            )
        except Exception as exc:
            logger.exception(
                "Ultralytics YOLO image analysis failed for evidence_id=%s",
                request.evidence_id,
            )
            raise ServiceUnavailableException(
                f"Vision provider failed: {str(exc)}"
            ) from exc

    def _get_or_create_model(self) -> YOLO:
        cache_key = (self.model_name, self.device or "auto")

        with self._model_cache_lock:
            cached_model = self._model_cache.get(cache_key)
            if cached_model is not None:
                return cached_model

            logger.info(
                "Loading Ultralytics YOLO model=%s device=%s",
                self.model_name,
                self.device or "auto",
            )
            model = YOLO(self.model_name)
            self._model_cache[cache_key] = model
            return model

    def _resolve_source(self, request: ImageAnalysisRequest) -> str:
        if request.image_file_path:
            return request.image_file_path

        if request.source_url:
            return request.source_url

        raise ConflictException("No image source was provided for visual analysis.")

    def _extract_detections(self, result: Any) -> list[dict[str, Any]]:
        boxes = getattr(result, "boxes", None)
        names = getattr(result, "names", {}) or {}

        if boxes is None or len(boxes) == 0:
            return []

        cls_values = boxes.cls.tolist() if hasattr(boxes.cls, "tolist") else list(boxes.cls)
        conf_values = boxes.conf.tolist() if hasattr(boxes.conf, "tolist") else list(boxes.conf)
        xyxy_values = boxes.xyxy.tolist() if hasattr(boxes.xyxy, "tolist") else list(boxes.xyxy)

        detections: list[dict[str, Any]] = []
        for cls_value, confidence, xyxy in zip(cls_values, conf_values, xyxy_values):
            class_id = int(cls_value)
            label = names.get(class_id, str(class_id))

            x1, y1, x2, y2 = xyxy
            detections.append(
                {
                    "class_id": class_id,
                    "label": label,
                    "confidence": round(float(confidence), 4),
                    "bbox_xyxy": {
                        "x1": round(float(x1), 2),
                        "y1": round(float(y1), 2),
                        "x2": round(float(x2), 2),
                        "y2": round(float(y2), 2),
                    },
                }
            )

        detections.sort(key=lambda item: item["confidence"], reverse=True)
        return detections

    def _extract_labels(self, detections: list[dict[str, Any]]) -> list[str]:
        if not detections:
            return []

        frequency_by_label = Counter()
        best_confidence_by_label = defaultdict(float)

        for detection in detections:
            label = detection["label"]
            frequency_by_label[label] += 1
            best_confidence_by_label[label] = max(
                best_confidence_by_label[label],
                detection["confidence"],
            )

        ordered_labels = sorted(
            frequency_by_label.keys(),
            key=lambda label: (
                -frequency_by_label[label],
                -best_confidence_by_label[label],
                label.lower(),
            ),
        )

        return ordered_labels

    def _build_summary(
        self,
        labels: list[str],
        detections: list[dict[str, Any]],
    ) -> str:
        if not detections:
            return (
                "No se detectaron objetos visibles con confianza suficiente en la imagen. "
                "La imagen puede requerir revisión manual o complementarse con texto y audio."
            )

        top_detections_text = ", ".join(
            f"{detection['label']} ({detection['confidence']:.2f})"
            for detection in detections[:3]
        )

        vehicle_labels = {"car", "truck", "bus", "motorcycle", "bicycle"}
        person_present = any(label.lower() == "person" for label in labels)
        vehicle_present = any(label.lower() in vehicle_labels for label in labels)
        multiple_vehicles = sum(
            1 for detection in detections if detection["label"].lower() in vehicle_labels
        ) >= 2

        summary_parts = [
            f"Objetos visibles detectados: {top_detections_text}.",
        ]

        if vehicle_present:
            summary_parts.append("Se observan elementos relacionados con vehículos en la escena.")

        if person_present:
            summary_parts.append("También se detecta al menos una persona en la escena.")

        if multiple_vehicles:
            summary_parts.append(
                "La presencia de múltiples vehículos puede indicar una situación vial o un incidente con más contexto visual."
            )

        summary_parts.append(
            "Este análisis visual es de apoyo y debe combinarse con audio y texto para la clasificación final del incidente."
        )

        return " ".join(summary_parts)

    def _infer_possible_incident_hint(
        self,
        labels: list[str],
        detections: list[dict[str, Any]],
    ) -> str:
        lowered_labels = {label.lower() for label in labels}

        vehicle_labels = {"car", "truck", "bus", "motorcycle", "bicycle"}
        vehicle_count = sum(
            1 for detection in detections if detection["label"].lower() in vehicle_labels
        )
        person_present = "person" in lowered_labels

        if vehicle_count >= 2 and person_present:
            return "POSSIBLE_ACCIDENT_SCENE"

        if vehicle_count >= 1:
            return "VEHICLE_PRESENT_BUT_MECHANICAL_CAUSE_NOT_DIRECTLY_VISIBLE"

        return "UNCERTAIN"
