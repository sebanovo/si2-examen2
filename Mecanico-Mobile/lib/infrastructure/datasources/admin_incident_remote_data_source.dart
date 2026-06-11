import 'package:dio/dio.dart';
import 'package:mechanic_mobile/core/network/api_client.dart';
import '../models/admin_incident_model.dart';

abstract class AdminIncidentRemoteDataSource {
  Future<List<AdminIncidentModel>> getAllIncidents();
  Future<AdminIncidentModel> getIncidentDetails(String incidentId);
  Future<List<CandidateModel>> getIncidentCandidates(String incidentId);
  Future<AdminIncidentModel> publishIncident(String incidentId);
}

class AdminIncidentRemoteDataSourceImpl
    implements AdminIncidentRemoteDataSource {
  final ApiClient _apiClient;

  AdminIncidentRemoteDataSourceImpl(this._apiClient);

  @override
  Future<List<AdminIncidentModel>> getAllIncidents() async {
    try {
      final response = await _apiClient.get('/api/incidents');
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final List<dynamic> data = jsonResponse['data'];
        return data.map((json) => AdminIncidentModel.fromJson(json)).toList();
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to load incidents');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<AdminIncidentModel> getIncidentDetails(String incidentId) async {
    try {
      final response = await _apiClient.get('/api/incidents/$incidentId');
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return AdminIncidentModel.fromJson(jsonResponse['data']);
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load incident details',
      );
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<List<CandidateModel>> getIncidentCandidates(String incidentId) async {
    try {
      final response = await _apiClient.get(
        '/api/assignment/platform/incidents/$incidentId/candidates',
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final List<dynamic> data = jsonResponse['data'];
        return data.map((json) => CandidateModel.fromJson(json)).toList();
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to load candidates');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<AdminIncidentModel> publishIncident(String incidentId) async {
    try {
      final response = await _apiClient.post(
        '/api/assignment/platform/incidents/$incidentId/publish',
        null,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final data = jsonResponse['data'];
        final publishedIncidentId = data['incident_id'] as String;
        return await getIncidentDetails(publishedIncidentId);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to publish incident');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
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
