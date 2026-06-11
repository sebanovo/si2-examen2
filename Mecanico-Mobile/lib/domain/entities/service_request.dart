class ServiceRequest {
  final String id;
  final String description;
  final String mechanicName;
  final String mechanicPhone;
  final String vehicleDetails;
  final String address;
  final String paymentMethod;
  final double totalCost;
  final String status; // e.g. Pending, En Route, In Progress, Completed
  final DateTime date;

  ServiceRequest({
    required this.id,
    required this.description,
    required this.mechanicName,
    required this.mechanicPhone,
    required this.vehicleDetails,
    required this.address,
    required this.paymentMethod,
    required this.totalCost,
    required this.status,
    required this.date,
  });
}
