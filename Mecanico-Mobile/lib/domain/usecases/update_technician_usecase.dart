import '../entities/technician.dart';

abstract class UpdateTechnicianUseCase {
  Future<Technician> execute(
    String technicianId,
    UpdateTechnicianParams params,
  );
}

class UpdateTechnicianParams {
  final String? firstName;
  final String? lastName;
  final String? phoneNumber;
  final String? specialty;
  final bool? isActive;
  final bool? isAvailable;
  final double? currentLatitude;
  final double? currentLongitude;

  UpdateTechnicianParams({
    this.firstName,
    this.lastName,
    this.phoneNumber,
    this.specialty,
    this.isActive,
    this.isAvailable,
    this.currentLatitude,
    this.currentLongitude,
  });

  Map<String, dynamic> toJson() => {
    if (firstName != null) 'first_name': firstName,
    if (lastName != null) 'last_name': lastName,
    if (phoneNumber != null) 'phone_number': phoneNumber,
    if (specialty != null) 'specialty': specialty,
    if (isActive != null) 'is_active': isActive,
    if (isAvailable != null) 'is_available': isAvailable,
    if (currentLatitude != null) 'current_latitude': currentLatitude,
    if (currentLongitude != null) 'current_longitude': currentLongitude,
  };
}
