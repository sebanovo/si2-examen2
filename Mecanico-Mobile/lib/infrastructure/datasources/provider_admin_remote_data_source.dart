import 'package:dio/dio.dart';
import 'package:mechanic_mobile/core/network/api_client.dart';
import '../models/provider_summary_model.dart';

abstract class ProviderAdminRemoteDataSource {
  Future<List<ProviderSummaryModel>> getProviders({
    int limit = 50,
    int offset = 0,
  });
}

class ProviderAdminRemoteDataSourceImpl
    implements ProviderAdminRemoteDataSource {
  final ApiClient _apiClient;

  ProviderAdminRemoteDataSourceImpl(this._apiClient);

  @override
  Future<List<ProviderSummaryModel>> getProviders({
    int limit = 50,
    int offset = 0,
  }) async {
    try {
      final response = await _apiClient.get(
        '/api/providers?limit=$limit&offset=$offset',
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final List<dynamic> data = jsonResponse['data'];
        return data.map((json) => ProviderSummaryModel.fromJson(json)).toList();
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to load providers');
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
