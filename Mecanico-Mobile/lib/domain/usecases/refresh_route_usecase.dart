import '../entities/tracking.dart';

abstract class RefreshRouteUseCase {
  Future<TrackingData> execute(String incidentId);
}
