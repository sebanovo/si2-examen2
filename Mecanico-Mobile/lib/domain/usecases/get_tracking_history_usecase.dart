import '../entities/tracking.dart';

abstract class GetTrackingHistoryUseCase {
  Future<List<TrackingHistoryItem>> execute(String incidentId);
}
