import '../entities/service_request.dart';
import '../repositories/service_request_repository.dart';

class GetServiceRequestsUseCase {
  final ServiceRequestRepository repository;

  GetServiceRequestsUseCase(this.repository);

  Future<List<ServiceRequest>> call() async {
    return await repository.getServiceRequests();
  }
}
