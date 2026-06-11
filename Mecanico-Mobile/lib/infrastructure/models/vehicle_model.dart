import '../../domain/entities/vehicle.dart';

class VehicleModel extends Vehicle {
  VehicleModel({
    required super.id,
    required super.ownerUserId,
    required super.plateNumber,
    required super.vehicleType,
    required super.brand,
    required super.model,
    required super.year,
    required super.color,
    required super.notes,
    required super.isActive,
    super.createdAt,
    super.updatedAt,
  });

  factory VehicleModel.fromJson(Map<String, dynamic> json) {
    return VehicleModel(
      id: (json['id'] ?? '').toString(),
      ownerUserId: (json['owner_user_id'] ?? '').toString(),
      plateNumber: (json['plate_number'] ?? '').toString(),
      vehicleType: (json['vehicle_type'] ?? '').toString(),
      brand: (json['brand'] ?? '').toString(),
      model: (json['model'] ?? '').toString(),
      year: (json['year'] ?? 0) as int,
      color: (json['color'] ?? '').toString(),
      notes: (json['notes'] ?? '').toString(),
      isActive: (json['is_active'] ?? true) as bool,
      createdAt: json['created_at'] != null
          ? DateTime.tryParse(json['created_at'].toString())
          : null,
      updatedAt: json['updated_at'] != null
          ? DateTime.tryParse(json['updated_at'].toString())
          : null,
    );
  }
}
