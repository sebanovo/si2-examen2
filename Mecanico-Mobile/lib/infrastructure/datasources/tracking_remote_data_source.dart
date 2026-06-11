import 'package:dio/dio.dart';
import 'package:mechanic_mobile/core/network/api_client.dart';
import '../models/tracking_model.dart';

abstract class TrackingRemoteDataSource {
  Future<TrackingDataModel> reportLocation(
    String incidentId,
    Map<String, dynamic> params,
  );
  Future<TrackingDataModel> refreshRoute(String incidentId);
  Future<TrackingDataModel> getLiveTracking(String incidentId);
  Future<List<TrackingHistoryItemModel>> getTrackingHistory(String incidentId);
  Future<TrackingDataModel> getClientLiveTracking(String incidentId);
  Future<List<TrackingHistoryItemModel>> getClientTrackingHistory(
    String incidentId,
  );
  Future<TrackingDataModel> getPlatformLiveTracking(String incidentId);
  Future<List<TrackingHistoryItemModel>> getPlatformTrackingHistory(
    String incidentId,
  );
}

class TrackingRemoteDataSourceImpl implements TrackingRemoteDataSource {
  final ApiClient _apiClient;

  TrackingRemoteDataSourceImpl(this._apiClient);

  @override
  Future<TrackingDataModel> reportLocation(
    String incidentId,
    Map<String, dynamic> params,
  ) async {
    try {
      final response = await _apiClient.post(
        '/api/tracking/provider/incidents/$incidentId/location',
        params,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return TrackingDataModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to report location');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<TrackingDataModel> refreshRoute(String incidentId) async {
    try {
      final response = await _apiClient.post(
        '/api/tracking/provider/incidents/$incidentId/refresh-route',
        null,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return TrackingDataModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to refresh route');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<TrackingDataModel> getLiveTracking(String incidentId) async {
    try {
      final response = await _apiClient.get(
        '/api/tracking/provider/incidents/$incidentId/live',
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return TrackingDataModel.fromJson(jsonResponse['data']);
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load live tracking',
      );
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<List<TrackingHistoryItemModel>> getTrackingHistory(
    String incidentId,
  ) async {
    try {
      final response = await _apiClient.get(
        '/api/tracking/provider/incidents/$incidentId/history',
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final List<dynamic> data = jsonResponse['data'];
        return data
            .map((json) => TrackingHistoryItemModel.fromJson(json))
            .toList();
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load tracking history',
      );
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<TrackingDataModel> getClientLiveTracking(String incidentId) async {
    try {
      final response = await _apiClient.get(
        '/api/tracking/client/incidents/$incidentId/live',
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return TrackingDataModel.fromJson(jsonResponse['data']);
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load client live tracking',
      );
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<List<TrackingHistoryItemModel>> getClientTrackingHistory(
    String incidentId,
  ) async {
    try {
      final response = await _apiClient.get(
        '/api/tracking/client/incidents/$incidentId/history',
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final List<dynamic> data = jsonResponse['data'];
        return data
            .map((json) => TrackingHistoryItemModel.fromJson(json))
            .toList();
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load client tracking history',
      );
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<TrackingDataModel> getPlatformLiveTracking(String incidentId) async {
    try {
      final response = await _apiClient.get(
        '/api/tracking/platform/incidents/$incidentId/live',
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return TrackingDataModel.fromJson(jsonResponse['data']);
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load platform live tracking',
      );
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<List<TrackingHistoryItemModel>> getPlatformTrackingHistory(
    String incidentId,
  ) async {
    try {
      final response = await _apiClient.get(
        '/api/tracking/platform/incidents/$incidentId/history',
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final List<dynamic> data = jsonResponse['data'];
        return data
            .map((json) => TrackingHistoryItemModel.fromJson(json))
            .toList();
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load platform tracking history',
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
