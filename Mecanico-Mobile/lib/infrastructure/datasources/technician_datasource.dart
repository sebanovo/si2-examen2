import 'package:dio/dio.dart';
import 'package:mechanic_mobile/core/network/api_client.dart';
import '../models/technician_model.dart';

abstract class TechnicianRemoteDataSource {
  Future<List<TechnicianModel>> getTechnicians();
  Future<TechnicianModel> createTechnician(Map<String, dynamic> params);
  Future<TechnicianModel> updateTechnician(
    String technicianId,
    Map<String, dynamic> params,
  );
}

class TechnicianRemoteDataSourceImpl implements TechnicianRemoteDataSource {
  final ApiClient _apiClient;

  TechnicianRemoteDataSourceImpl(this._apiClient);

  @override
  Future<List<TechnicianModel>> getTechnicians() async {
    try {
      final response = await _apiClient.get('/api/providers/me/technicians');
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final List<dynamic> data = jsonResponse['data'];
        return data.map((json) => TechnicianModel.fromJson(json)).toList();
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to load technicians');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<TechnicianModel> createTechnician(Map<String, dynamic> params) async {
    try {
      final response = await _apiClient.post(
        '/api/providers/me/technicians',
        params,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return TechnicianModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to create technician');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<TechnicianModel> updateTechnician(
    String technicianId,
    Map<String, dynamic> params,
  ) async {
    try {
      final response = await _apiClient.patch(
        '/api/providers/me/technicians/$technicianId',
        params,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return TechnicianModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to update technician');
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
