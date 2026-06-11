import 'package:dio/dio.dart';
import 'package:mechanic_mobile/core/network/api_client.dart';
import '../models/device_token_model.dart';

abstract class NotificationRemoteDataSource {
  Future<DeviceTokenModel> registerDevice(Map<String, dynamic> params);
  Future<DeviceTokenModel> unregisterDevice(String deviceTokenId);
  Future<List<DeviceTokenModel>> getMyDevices();
}

class NotificationRemoteDataSourceImpl implements NotificationRemoteDataSource {
  final ApiClient _apiClient;

  NotificationRemoteDataSourceImpl(this._apiClient);

  @override
  Future<DeviceTokenModel> registerDevice(Map<String, dynamic> params) async {
    try {
      final response = await _apiClient.post(
        '/api/notifications/me/devices/register',
        params,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return DeviceTokenModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to register device');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<DeviceTokenModel> unregisterDevice(String deviceTokenId) async {
    try {
      final response = await _apiClient.delete(
        '/api/notifications/me/devices/$deviceTokenId',
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return DeviceTokenModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to unregister device');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<List<DeviceTokenModel>> getMyDevices() async {
    try {
      final response = await _apiClient.get('/api/notifications/me/devices');
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final List<dynamic> data = jsonResponse['data'];
        return data.map((json) => DeviceTokenModel.fromJson(json)).toList();
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to load devices');
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
