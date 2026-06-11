import 'package:flutter/material.dart';
import '../../domain/entities/tracking.dart';
import '../../domain/usecases/report_location_usecase.dart';
import '../../domain/usecases/refresh_route_usecase.dart';
import '../../domain/usecases/get_live_tracking_usecase.dart';
import '../../domain/usecases/get_tracking_history_usecase.dart';

class ProviderTrackingViewModel extends ChangeNotifier {
  final ReportLocationUseCase _reportLocationUseCase;
  final RefreshRouteUseCase _refreshRouteUseCase;
  final GetLiveTrackingUseCase _getLiveTrackingUseCase;
  final GetTrackingHistoryUseCase _getTrackingHistoryUseCase;

  TrackingData? _trackingData;
  List<TrackingHistoryItem> _history = [];
  bool _isLoading = false;
  String? _errorMessage;

  ProviderTrackingViewModel({
    required ReportLocationUseCase reportLocationUseCase,
    required RefreshRouteUseCase refreshRouteUseCase,
    required GetLiveTrackingUseCase getLiveTrackingUseCase,
    required GetTrackingHistoryUseCase getTrackingHistoryUseCase,
  }) : _reportLocationUseCase = reportLocationUseCase,
       _refreshRouteUseCase = refreshRouteUseCase,
       _getLiveTrackingUseCase = getLiveTrackingUseCase,
       _getTrackingHistoryUseCase = getTrackingHistoryUseCase;

  TrackingData? get trackingData => _trackingData;
  List<TrackingHistoryItem> get history => _history;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  Future<void> loadLiveTracking(String incidentId) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _trackingData = await _getLiveTrackingUseCase.execute(incidentId);
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<void> loadTrackingHistory(String incidentId) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _history = await _getTrackingHistoryUseCase.execute(incidentId);
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<TrackingData?> reportLocation({
    required String incidentId,
    required double latitude,
    required double longitude,
    required String technicianId,
    double? accuracyMeters,
  }) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final params = ReportLocationParams(
        latitude: latitude,
        longitude: longitude,
        accuracyMeters: accuracyMeters,
        technicianId: technicianId,
      );
      final result = await _reportLocationUseCase.execute(incidentId, params);
      _trackingData = result;
      notifyListeners();
      return result;
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
      return null;
    } finally {
      _setLoading(false);
    }
  }

  Future<TrackingData?> refreshRoute(String incidentId) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final result = await _refreshRouteUseCase.execute(incidentId);
      _trackingData = result;
      notifyListeners();
      return result;
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
      return null;
    } finally {
      _setLoading(false);
    }
  }

  void _setLoading(bool loading) {
    _isLoading = loading;
    notifyListeners();
  }

  void clearError() {
    _errorMessage = null;
    notifyListeners();
  }

  void clearTrackingData() {
    _trackingData = null;
    _history = [];
    notifyListeners();
  }
}
