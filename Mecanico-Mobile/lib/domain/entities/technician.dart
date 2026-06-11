class Technician {
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

  Technician({
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

  String get fullName => '$firstName $lastName';
  String get location => currentLatitude != null && currentLongitude != null
      ? 'Lat: ${currentLatitude!.toStringAsFixed(4)}, Lng: ${currentLongitude!.toStringAsFixed(4)}'
      : 'Sin ubicación';
}
