import '../../domain/entities/user.dart';

class UserModel extends User {
  UserModel({
    required super.id,
    required super.email,
    required super.fullName,
    super.firstName,
    super.lastName,
    super.phoneNumber,
    super.isActive,
    super.isSuperuser,
    super.roleCodes,
    super.createdAt,
    super.updatedAt,
  });

  factory UserModel.fromJson(Map<String, dynamic> json) {
    final firstName = json['first_name'] as String?;
    final lastName = json['last_name'] as String?;
    final fullName =
        (json['full_name'] as String?)?.trim().isNotEmpty == true
        ? json['full_name'] as String
        : '${firstName ?? ''} ${lastName ?? ''}'.trim();

    return UserModel(
      id: json['id'],
      email: json['email'],
      fullName: fullName,
      firstName: firstName,
      lastName: lastName,
      phoneNumber: json['phone_number'] as String?,
      isActive: json['is_active'] as bool?,
      isSuperuser: json['is_superuser'] as bool?,
      roleCodes: ((json['role_codes'] as List?) ?? const [])
          .map((e) => e.toString())
          .toList(),
      createdAt: json['created_at'] != null
          ? DateTime.tryParse(json['created_at'])
          : null,
      updatedAt: json['updated_at'] != null
          ? DateTime.tryParse(json['updated_at'])
          : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'email': email,
      'full_name': fullName,
      'first_name': firstName,
      'last_name': lastName,
      'phone_number': phoneNumber,
      'is_active': isActive,
      'is_superuser': isSuperuser,
      'role_codes': roleCodes,
      'created_at': createdAt?.toIso8601String(),
      'updated_at': updatedAt?.toIso8601String(),
    };
  }
}
