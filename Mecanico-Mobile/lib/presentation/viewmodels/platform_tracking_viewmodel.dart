import 'package:flutter/material.dart';
import '../../domain/entities/tracking.dart';
import '../../infrastructure/datasources/tracking_remote_data_source.dart';

class PlatformTrackingViewModel extends ChangeNotifier {
  final TrackingRemoteDataSource _dataSource;

  TrackingData? _trackingData;
  List<TrackingHistoryItem> _history = [];
  bool _isLoading = false;
  String? _errorMessage;

  PlatformTrackingViewModel(this._dataSource);

  TrackingData? get trackingData => _trackingData;
  List<TrackingHistoryItem> get history => _history;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  Future<void> loadLiveTracking(String incidentId) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final model = await _dataSource.getPlatformLiveTracking(incidentId);
      _trackingData = model.toEntity();
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
      final models = await _dataSource.getPlatformTrackingHistory(incidentId);
      _history = models.map((m) => m.toEntity()).toList();
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
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
