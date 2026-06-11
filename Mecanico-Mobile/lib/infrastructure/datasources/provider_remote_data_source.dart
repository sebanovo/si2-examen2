import 'package:dio/dio.dart';
import 'package:mechanic_mobile/core/network/api_client.dart';
import '../models/provider_profile_model.dart';

abstract class ProviderRemoteDataSource {
  Future<ProviderProfileModel> getProviderProfile();
  Future<ProviderProfileModel> updateProviderProfile(
    Map<String, dynamic> params,
  );
}

class ProviderRemoteDataSourceImpl implements ProviderRemoteDataSource {
  final ApiClient _apiClient;

  ProviderRemoteDataSourceImpl(this._apiClient);

  @override
  Future<ProviderProfileModel> getProviderProfile() async {
    try {
      final response = await _apiClient.get('/api/providers/me/profile');
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return ProviderProfileModel.fromJson(jsonResponse['data']);
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load provider profile',
      );
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<ProviderProfileModel> updateProviderProfile(
    Map<String, dynamic> params,
  ) async {
    try {
      final response = await _apiClient.patch(
        '/api/providers/me/profile',
        params,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return ProviderProfileModel.fromJson(jsonResponse['data']);
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to update provider profile',
      );
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
