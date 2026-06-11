from typing import Literal

from pydantic import BaseModel, Field


class ClientCreateCheckoutRequest(BaseModel):
    payment_method: Literal["QR", "GATEWAY", "TRANSFER", "CARD"] = "QR"
    return_url: str | None = Field(default=None, max_length=500)


class ClientSimulatePaymentSuccessRequest(BaseModel):
    payment_reference: str | None = Field(default=None, max_length=255)


class ClientSimulatePaymentFailureRequest(BaseModel):
    failure_reason: str = Field(
        default="Pago rechazado por el proveedor simulado.",
        min_length=3,
        max_length=500,
    )