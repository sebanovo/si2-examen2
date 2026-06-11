import '../../domain/entities/technician.dart';

class TechnicianModel {
  final String id;
  final String firstName;
  final String lastName;
  final String phoneNumber;
  final String specialty;
  final bool isAvailable;
  final double? currentLatitude;
  final double? currentLongitude;
  final DateTime? createdAt;
  final DateTime? updatedAt;

  TechnicianModel({
    required this.id,
    required this.firstName,
    required this.lastName,
    required this.phoneNumber,
    required this.specialty,
    required this.isAvailable,
    this.currentLatitude,
    this.currentLongitude,
    this.createdAt,
    this.updatedAt,
  });

  factory TechnicianModel.fromJson(Map<String, dynamic> json) {
    return TechnicianModel(
      id: json['id'] as String,
      firstName: json['first_name'] as String,
      lastName: json['last_name'] as String,
      phoneNumber: json['phone_number'] as String,
      specialty: json['specialty'] as String? ?? '',
      isAvailable: json['is_available'] as bool? ?? false,
      currentLatitude: (json['current_latitude'] as num?)?.toDouble(),
      currentLongitude: (json['current_longitude'] as num?)?.toDouble(),
      createdAt: json['created_at'] != null
          ? DateTime.parse(json['created_at'] as String)
          : null,
      updatedAt: json['updated_at'] != null
          ? DateTime.parse(json['updated_at'] as String)
          : null,
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'first_name': firstName,
    'last_name': lastName,
    'phone_number': phoneNumber,
    'specialty': specialty,
    'is_available': isAvailable,
    if (currentLatitude != null) 'current_latitude': currentLatitude,
    if (currentLongitude != null) 'current_longitude': currentLongitude,
    if (createdAt != null) 'created_at': createdAt?.toIso8601String(),
    if (updatedAt != null) 'updated_at': updatedAt?.toIso8601String(),
  };

  Technician toEntity() => Technician(
    id: id,
    firstName: firstName,
    lastName: lastName,
    phoneNumber: phoneNumber,
    specialty: specialty,
    isAvailable: isAvailable,
    currentLatitude: currentLatitude,
    currentLongitude: currentLongitude,
    createdAt: createdAt,
    updatedAt: updatedAt,
  );

  static TechnicianModel fromEntity(Technician entity) => TechnicianModel(
    id: entity.id,
    firstName: entity.firstName,
    lastName: entity.lastName,
    phoneNumber: entity.phoneNumber,
    specialty: entity.specialty,
    isAvailable: entity.isAvailable,
    currentLatitude: entity.currentLatitude,
    currentLongitude: entity.currentLongitude,
    createdAt: entity.createdAt,
    updatedAt: entity.updatedAt,
  );
}
