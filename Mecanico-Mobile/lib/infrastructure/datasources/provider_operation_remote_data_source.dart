import 'package:dio/dio.dart';
import 'package:mechanic_mobile/core/network/api_client.dart';
import '../models/provider_operation_model.dart';

abstract class ProviderOperationRemoteDataSource {
  Future<List<ProviderOperationModel>> getActiveOperations();
  Future<ProviderOperationModel> getOperationState(String incidentId);
  Future<ProviderOperationModel> dispatchIncident(
    String incidentId,
    Map<String, dynamic> params,
  );
  Future<ProviderOperationModel> markArrived(String incidentId, {String? note});
  Future<ProviderOperationModel> startService(
    String incidentId, {
    String? note,
  });
  Future<ProviderOperationModel> completeService(
    String incidentId,
    Map<String, dynamic> params,
  );
  Future<ProviderOperationModel> cancelService(
    String incidentId, {
    String? note,
  });
}

class ProviderOperationRemoteDataSourceImpl
    implements ProviderOperationRemoteDataSource {
  final ApiClient _apiClient;

  ProviderOperationRemoteDataSourceImpl(this._apiClient);

  @override
  Future<List<ProviderOperationModel>> getActiveOperations() async {
    try {
      final response = await _apiClient.get(
        '/api/operations/provider/me/active',
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        final List<dynamic> data = jsonResponse['data'];
        return data
            .map((json) => ProviderOperationModel.fromJson(json))
            .toList();
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load active operations',
      );
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<ProviderOperationModel> getOperationState(String incidentId) async {
    try {
      final response = await _apiClient.get(
        '/api/operations/provider/incidents/$incidentId/state',
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return ProviderOperationModel.fromJson(jsonResponse['data']);
      }
      throw Exception(
        jsonResponse['message'] ?? 'Failed to load operation state',
      );
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<ProviderOperationModel> dispatchIncident(
    String incidentId,
    Map<String, dynamic> params,
  ) async {
    try {
      final response = await _apiClient.post(
        '/api/operations/provider/incidents/$incidentId/dispatch',
        params,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return ProviderOperationModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to dispatch incident');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<ProviderOperationModel> markArrived(
    String incidentId, {
    String? note,
  }) async {
    try {
      final body = note != null ? {'note': note} : {};
      final response = await _apiClient.post(
        '/api/operations/provider/incidents/$incidentId/arrive',
        body,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return ProviderOperationModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to mark arrival');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<ProviderOperationModel> startService(
    String incidentId, {
    String? note,
  }) async {
    try {
      final body = note != null ? {'note': note} : {};
      final response = await _apiClient.post(
        '/api/operations/provider/incidents/$incidentId/start',
        body,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return ProviderOperationModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to start service');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<ProviderOperationModel> completeService(
    String incidentId,
    Map<String, dynamic> params,
  ) async {
    try {
      final response = await _apiClient.post(
        '/api/operations/provider/incidents/$incidentId/complete',
        params,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return ProviderOperationModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to complete service');
    } on DioException catch (e) {
      throw Exception(_getErrorMessage(e));
    }
  }

  @override
  Future<ProviderOperationModel> cancelService(
    String incidentId, {
    String? note,
  }) async {
    try {
      final body = note != null ? {'note': note} : {};
      final response = await _apiClient.post(
        '/api/operations/provider/incidents/$incidentId/cancel',
        body,
      );
      final Map<String, dynamic> jsonResponse =
          response.data as Map<String, dynamic>;
      if (jsonResponse['success'] == true) {
        return ProviderOperationModel.fromJson(jsonResponse['data']);
      }
      throw Exception(jsonResponse['message'] ?? 'Failed to cancel service');
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
