class User {
  final String id;
  final String email;
  final String fullName;
  final String? firstName;
  final String? lastName;
  final String? phoneNumber;
  final bool? isActive;
  final bool? isSuperuser;
  final List<String> roleCodes;
  final DateTime? createdAt;
  final DateTime? updatedAt;

  User({
    required this.id,
    required this.email,
    required this.fullName,
    this.firstName,
    this.lastName,
    this.phoneNumber,
    this.isActive,
    this.isSuperuser,
    this.roleCodes = const [],
    this.createdAt,
    this.updatedAt,
  });
}
