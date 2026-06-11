import '../../domain/entities/user.dart';

class Evidence {
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

  Evidence({
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

  bool get isText => evidenceType == 'TEXT';
  bool get isImage => evidenceType == 'IMAGE';
  bool get isAudio => evidenceType == 'AUDIO';

  String get fileSizeFormatted {
    if (fileSizeBytes == null) return 'N/A';
    if (fileSizeBytes! < 1024) return '$fileSizeBytes B';
    if (fileSizeBytes! < 1024 * 1024) {
      return '${(fileSizeBytes! / 1024).toStringAsFixed(1)} KB';
    }
    return '${(fileSizeBytes! / (1024 * 1024)).toStringAsFixed(1)} MB';
  }
}
