import '../entities/service_request.dart';

abstract class ServiceRequestRepository {
  Future<List<ServiceRequest>> getServiceRequests();
  Future<ServiceRequest> getServiceRequestById(String id);
}
