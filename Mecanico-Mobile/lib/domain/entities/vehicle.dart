class Vehicle {
  final String id;
  final String ownerUserId;
  final String plateNumber;
  final String vehicleType;
  final String brand;
  final String model;
  final int year;
  final String color;
  final String notes;
  final bool isActive;
  final DateTime? createdAt;
  final DateTime? updatedAt;

  Vehicle({
    required this.id,
    required this.ownerUserId,
    required this.plateNumber,
    required this.vehicleType,
    required this.brand,
    required this.model,
    required this.year,
    required this.color,
    required this.notes,
    required this.isActive,
    this.createdAt,
    this.updatedAt,
  });
}
