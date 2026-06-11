import '../../domain/entities/service_request.dart';

class ServiceRequestModel extends ServiceRequest {
  ServiceRequestModel({
    required super.id,
    required super.description,
    required super.mechanicName,
    required super.mechanicPhone,
    required super.vehicleDetails,
    required super.address,
    required super.paymentMethod,
    required super.totalCost,
    required super.status,
    required super.date,
  });

  factory ServiceRequestModel.fromJson(Map<String, dynamic> json) {
    return ServiceRequestModel(
      id: json['id'],
      description: json['description'],
      mechanicName: json['mechanicName'],
      mechanicPhone: json['mechanicPhone'],
      vehicleDetails: json['vehicleDetails'],
      address: json['address'],
      paymentMethod: json['paymentMethod'],
      totalCost: (json['totalCost'] as num).toDouble(),
      status: json['status'],
      date: DateTime.parse(json['date']),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'description': description,
      'mechanicName': mechanicName,
      'mechanicPhone': mechanicPhone,
      'vehicleDetails': vehicleDetails,
      'address': address,
      'paymentMethod': paymentMethod,
      'totalCost': totalCost,
      'status': status,
      'date': date.toIso8601String(),
    };
  }
}
