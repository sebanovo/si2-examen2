import 'package:dio/dio.dart';
import 'package:mechanic_mobile/core/network/api_client.dart';
import '../models/provider_candidate_model.dart';

abstract class ProviderAssignmentRemoteDataSource {
  Future<List<ProviderCandidateModel>> getAvailableCandidates();
  Future<ProviderCandidateModel> getCandidateDetails(String candidateId);
  Future<Map<String, dynamic>> acceptCandidate(String candidateId);
  Future<void> rejectCandidate(String candidateId);
}

class ProviderAssignmentRemoteDataSourceImpl
    implements ProviderAssignmentRemoteDataSource {
  final ApiClient _apiClient;

  ProviderAssignmentRemoteDataSourceImpl(this._apiClient);

  @override
  Future<List<ProviderCandidateModel>> getAvailableCandidates() async {
    try {
      final response = await _apiClient.get(
        '/api/assignment/provider/me/available',
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final List<dynamic> data = jsonResponse['data'];
        return data
            .map((json) => ProviderCandidateModel.fromJson(json))
            .toList();
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load available candidates',
      );
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<ProviderCandidateModel> getCandidateDetails(String candidateId) async {
    try {
      final response = await _apiClient.get(
        '/api/assignment/provider/me/available/$candidateId',
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return ProviderCandidateModel.fromJson(jsonResponse['data']);
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load candidate details',
      );
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<Map<String, dynamic>> acceptCandidate(String candidateId) async {
    try {
      final response = await _apiClient.post(
        '/api/assignment/provider/me/available/$candidateId/accept',
        null,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return jsonResponse['data'] as Map<String, dynamic>;
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to accept candidate');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<void> rejectCandidate(String candidateId) async {
    try {
      final response = await _apiClient.post(
        '/api/assignment/provider/me/available/$candidateId/reject',
        null,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] != true) {
        throw Exception(
          jsonResponse['message'] ?? 'Failed to reject candidate',
        );
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
