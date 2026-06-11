import '../entities/tracking.dart';

abstract class GetLiveTrackingUseCase {
  Future<TrackingData> execute(String incidentId);
}
