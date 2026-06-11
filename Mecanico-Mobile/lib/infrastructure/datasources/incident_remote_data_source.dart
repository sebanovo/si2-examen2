import 'package:dio/dio.dart';
import 'package:mechanic_mobile/core/network/api_client.dart';
import '../models/incident_model.dart';

abstract class IncidentRemoteDataSource {
  Future<List<IncidentModel>> getMyIncidents();
  Future<IncidentModel> createIncident(Map<String, dynamic> params);
  Future<IncidentModel> updateIncident(
    String incidentId,
    Map<String, dynamic> params,
  );
  Future<void> cancelIncident(String incidentId);
}

class IncidentRemoteDataSourceImpl implements IncidentRemoteDataSource {
  final ApiClient _apiClient;

  IncidentRemoteDataSourceImpl(this._apiClient);

  @override
  Future<List<IncidentModel>> getMyIncidents() async {
    try {
      final response = await _apiClient.get('/api/incidents/me');
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final List<dynamic> data = jsonResponse['data'];
        return data.map((json) => IncidentModel.fromJson(json)).toList();
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to load incidents');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<IncidentModel> createIncident(Map<String, dynamic> params) async {
    try {
      final response = await _apiClient.post('/api/incidents', params);
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return IncidentModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to create incident');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<IncidentModel> updateIncident(
    String incidentId,
    Map<String, dynamic> params,
  ) async {
    try {
      final response = await _apiClient.patch(
        '/api/incidents/me/$incidentId',
        params,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return IncidentModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to update incident');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<void> cancelIncident(String incidentId) async {
    try {
      final response = await _apiClient.post(
        '/api/incidents/me/$incidentId/cancel',
        null,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] != true) {
        throw Exception(jsonResponse['message'] ?? 'Failed to cancel incident');
      }
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
