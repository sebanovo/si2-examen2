import '../entities/technician.dart';

abstract class CreateTechnicianUseCase {
  Future<Technician> execute(CreateTechnicianParams params);
}

class CreateTechnicianParams {
  final String firstName;
  final String lastName;
  final String phoneNumber;
  final String specialty;
  final bool isAvailable;
  final double? currentLatitude;
  final double? currentLongitude;

  CreateTechnicianParams({
    required this.firstName,
    required this.lastName,
    required this.phoneNumber,
    required this.specialty,
    required this.isAvailable,
    this.currentLatitude,
    this.currentLongitude,
  });

  Map<String, dynamic> toJson() => {
    'first_name': firstName,
    'last_name': lastName,
    'phone_number': phoneNumber,
    'specialty': specialty,
    'is_available': isAvailable,
    if (currentLatitude != null) 'current_latitude': currentLatitude,
    if (currentLongitude != null) 'current_longitude': currentLongitude,
  };
}
