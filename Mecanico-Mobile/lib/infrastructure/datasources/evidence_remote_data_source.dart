import 'package:dio/dio.dart';
import 'package:image_picker/image_picker.dart';
import 'package:mechanic_mobile/core/network/api_client.dart';
import '../models/evidence_model.dart';

abstract class EvidenceRemoteDataSource {
  Future<EvidenceModel> addTextEvidence(
    String incidentId,
    Map<String, dynamic> params,
  );
  Future<EvidenceModel> addFileEvidence(
    String incidentId,
    String evidenceType,
    String description,
    XFile file,
  );
}

class EvidenceRemoteDataSourceImpl implements EvidenceRemoteDataSource {
  final ApiClient _apiClient;

  EvidenceRemoteDataSourceImpl(this._apiClient);

  @override
  Future<EvidenceModel> addTextEvidence(
    String incidentId,
    Map<String, dynamic> params,
  ) async {
    try {
      final response = await _apiClient.post(
        '/api/evidences/client/incidents/$incidentId/text',
        params,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return EvidenceModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to add text evidence');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<EvidenceModel> addFileEvidence(
    String incidentId,
    String evidenceType,
    String description,
    XFile file,
  ) async {
    try {
      final fileName = file.name;
      final bytes = await file.readAsBytes();

      final extension = fileName.split('.').last.toLowerCase();
      final mimeType = evidenceType == 'IMAGE'
          ? (extension == 'png' ? 'image/png' : 'image/jpeg')
          : 'audio/mpeg';

      final additionalFields = {
        'evidence_type': evidenceType,
        'description': description,
      };

      final response = await _apiClient.uploadFile(
        '/api/evidences/client/incidents/$incidentId/files',
        fieldName: 'upload_file',
        fileName: fileName,
        bytes: bytes,
        mimeType: mimeType,
        additionalFields: additionalFields,
      );

      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return EvidenceModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to add file evidence');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    } catch (e) {
      throw Exception('Error al subir el archivo: $e');
    }
  }

  String _getErrorMessage(DioException e) {
    if (e.response != null) {
      final data = e.response?.data;
      if (data != null && data['message'] != null) {
        return data['message'] as String;
      }
      return 'Error del servidor: ${e.response?.statusCode}';
    }
    return 'Error de red: ${e.message}';
  }
}
