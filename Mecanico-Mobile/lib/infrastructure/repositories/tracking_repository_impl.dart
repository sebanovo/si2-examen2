import '../../domain/entities/tracking.dart';
import '../../domain/usecases/report_location_usecase.dart';
import '../../domain/usecases/refresh_route_usecase.dart';
import '../../domain/usecases/get_live_tracking_usecase.dart';
import '../../domain/usecases/get_tracking_history_usecase.dart';
import '../datasources/tracking_remote_data_source.dart';

class TrackingRepository {
  final TrackingRemoteDataSource _dataSource;

  TrackingRepository(this._dataSource);

  Future<TrackingData> reportLocation(
    String incidentId,
    ReportLocationParams params,
  ) async {
    final model = await _dataSource.reportLocation(incidentId, params.toJson());
    return model.toEntity();
  }

  Future<TrackingData> refreshRoute(String incidentId) async {
    final model = await _dataSource.refreshRoute(incidentId);
    return model.toEntity();
  }

  Future<TrackingData> getLiveTracking(String incidentId) async {
    final model = await _dataSource.getLiveTracking(incidentId);
    return model.toEntity();
  }

  Future<List<TrackingHistoryItem>> getTrackingHistory(
    String incidentId,
  ) async {
    final models = await _dataSource.getTrackingHistory(incidentId);
    return models.map((model) => model.toEntity()).toList();
  }
}

// Implementación de UseCases
class ReportLocationUseCaseImpl implements ReportLocationUseCase {
  final TrackingRepository _repository;

  ReportLocationUseCaseImpl(this._repository);

  @override
  Future<TrackingData> execute(
    String incidentId,
    ReportLocationParams params,
  ) async {
    return await _repository.reportLocation(incidentId, params);
  }
}

class RefreshRouteUseCaseImpl implements RefreshRouteUseCase {
  final TrackingRepository _repository;

  RefreshRouteUseCaseImpl(this._repository);

  @override
  Future<TrackingData> execute(String incidentId) async {
    return await _repository.refreshRoute(incidentId);
  }
}

class GetLiveTrackingUseCaseImpl implements GetLiveTrackingUseCase {
  final TrackingRepository _repository;

  GetLiveTrackingUseCaseImpl(this._repository);

  @override
  Future<TrackingData> execute(String incidentId) async {
    return await _repository.getLiveTracking(incidentId);
  }
}

class GetTrackingHistoryUseCaseImpl implements GetTrackingHistoryUseCase {
  final TrackingRepository _repository;

  GetTrackingHistoryUseCaseImpl(this._repository);

  @override
  Future<List<TrackingHistoryItem>> execute(String incidentId) async {
    return await _repository.getTrackingHistory(incidentId);
  }
}
