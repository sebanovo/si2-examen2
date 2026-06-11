import 'package:dio/dio.dart';
import 'package:mechanic_mobile/core/network/api_client.dart';
import '../models/catalog_service_model.dart';

abstract class CatalogRemoteDataSource {
  Future<List<CatalogServiceEntryModel>> getCatalogServices();
  Future<List<ProviderServiceModel>> getProviderServices();
  Future<ProviderServiceModel> createProviderService(
    Map<String, dynamic> params,
  );
}

class CatalogRemoteDataSourceImpl implements CatalogRemoteDataSource {
  final ApiClient _apiClient;

  CatalogRemoteDataSourceImpl(this._apiClient);

  @override
  Future<List<CatalogServiceEntryModel>> getCatalogServices() async {
    try {
      final response = await _apiClient.get('/api/catalog/me/services/catalog');
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final List<dynamic> data = jsonResponse['data'];
        return data
            .map((json) => CatalogServiceEntryModel.fromJson(json))
            .toList();
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load catalog services',
      );
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<List<ProviderServiceModel>> getProviderServices() async {
    try {
      final response = await _apiClient.get('/api/catalog/me/services');
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final List<dynamic> data = jsonResponse['data'];
        return data.map((json) => ProviderServiceModel.fromJson(json)).toList();
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load provider services',
      );
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<ProviderServiceModel> createProviderService(
    Map<String, dynamic> params,
  ) async {
    try {
      final response = await _apiClient.post(
        '/api/catalog/me/services',
        params,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return ProviderServiceModel.fromJson(jsonResponse['data']);
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to create provider service',
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
