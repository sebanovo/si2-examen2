import '../../domain/entities/evidence.dart';
import '../../domain/entities/user.dart';

class EvidenceModel {
  final String id;
  final String incidentId;
  final String uploadedByUserId;
  final String evidenceType;
  final String? originalFilename;
  final String storedFilename;
  final String? fileExtension;
  final String? mimeType;
  final int? fileSizeBytes;
  final String? description;
  final String? textContentSnapshot;
  final String storageProvider;
  final String? downloadUrl;
  final String? audioProcessingStatus;
  final String? transcriptText;
  final String? imageProcessingStatus;
  final String? imageSummary;
  final DateTime createdAt;
  final DateTime updatedAt;
  final User? uploadedByUser;

  EvidenceModel({
    required this.id,
    required this.incidentId,
    required this.uploadedByUserId,
    required this.evidenceType,
    this.originalFilename,
    required this.storedFilename,
    this.fileExtension,
    this.mimeType,
    this.fileSizeBytes,
    this.description,
    this.textContentSnapshot,
    required this.storageProvider,
    this.downloadUrl,
    this.audioProcessingStatus,
    this.transcriptText,
    this.imageProcessingStatus,
    this.imageSummary,
    required this.createdAt,
    required this.updatedAt,
    this.uploadedByUser,
  });

  factory EvidenceModel.fromJson(Map<String, dynamic> json) {
    return EvidenceModel(
      id: _toStringOrFallback(json['id'], ''),
      incidentId: _toStringOrFallback(json['incident_id'], ''),
      uploadedByUserId: _toStringOrFallback(json['uploaded_by_user_id'], ''),
      evidenceType: _toStringOrFallback(json['evidence_type'], 'TEXT'),
      originalFilename: json['original_filename'] as String?,
      storedFilename: _toStringOrFallback(json['stored_filename'], ''),
      fileExtension: json['file_extension'] as String?,
      mimeType: json['mime_type'] as String?,
      fileSizeBytes: json['file_size_bytes'] as int?,
      description: json['description'] as String?,
      textContentSnapshot: json['text_content_snapshot'] as String?,
      storageProvider: _toStringOrFallback(json['storage_provider'], 'local'),
      downloadUrl: json['download_url'] as String?,
      audioProcessingStatus: json['audio_processing_status'] as String?,
      transcriptText: json['transcript_text'] as String?,
      imageProcessingStatus: json['image_processing_status'] as String?,
      imageSummary: json['image_summary'] as String?,
      createdAt: json['created_at'] != null
          ? DateTime.parse(json['created_at'] as String)
          : DateTime.now(),
      updatedAt: json['updated_at'] != null
          ? DateTime.parse(json['updated_at'] as String)
          : DateTime.now(),
      uploadedByUser: json['uploaded_by_user'] != null
          ? _parseUser(json['uploaded_by_user'])
          : null,
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }

  static User _parseUser(Map<String, dynamic> json) {
    return User(
      id: _toStringOrFallback(json['id'], ''),
      email: _toStringOrFallback(json['email'], ''),
      fullName: _toStringOrFallback(json['full_name'], ''),
      firstName: json['first_name'] as String?,
      lastName: json['last_name'] as String?,
      phoneNumber: json['phone_number'] as String?,
      isActive: json['is_active'] as bool? ?? true,
      isSuperuser: json['is_superuser'] as bool? ?? false,
      roleCodes: json['role_codes'] != null
          ? List<String>.from(json['role_codes'] as List)
          : [],
    );
  }

  Evidence toEntity() {
    return Evidence(
      id: id,
      incidentId: incidentId,
      uploadedByUserId: uploadedByUserId,
      evidenceType: evidenceType,
      originalFilename: originalFilename,
      storedFilename: storedFilename,
      fileExtension: fileExtension,
      mimeType: mimeType,
      fileSizeBytes: fileSizeBytes,
      description: description,
      textContentSnapshot: textContentSnapshot,
      storageProvider: storageProvider,
      downloadUrl: downloadUrl,
      audioProcessingStatus: audioProcessingStatus,
      transcriptText: transcriptText,
      imageProcessingStatus: imageProcessingStatus,
      imageSummary: imageSummary,
      createdAt: createdAt,
      updatedAt: updatedAt,
      uploadedByUser: uploadedByUser,
    );
  }
}
