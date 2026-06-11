import '../../domain/entities/device_token.dart';

class DeviceTokenModel {
  final String id;
  final String userId;
  final String devicePlatform;
  final String? deviceLabel;
  final String appRole;
  final String pushProviderName;
  final bool isActive;
  final DateTime lastSeenAt;
  final DateTime createdAt;
  final DateTime updatedAt;

  DeviceTokenModel({
    required this.id,
    required this.userId,
    required this.devicePlatform,
    this.deviceLabel,
    required this.appRole,
    required this.pushProviderName,
    required this.isActive,
    required this.lastSeenAt,
    required this.createdAt,
    required this.updatedAt,
  });

  factory DeviceTokenModel.fromJson(Map<String, dynamic> json) {
    return DeviceTokenModel(
      id: _toStringOrFallback(json['id'], ''),
      userId: _toStringOrFallback(json['user_id'], ''),
      devicePlatform: _toStringOrFallback(json['device_platform'], 'UNKNOWN'),
      deviceLabel: json['device_label'] as String?,
      appRole: _toStringOrFallback(json['app_role'], 'CLIENT'),
      pushProviderName: _toStringOrFallback(json['push_provider_name'], ''),
      isActive: json['is_active'] as bool? ?? true,
      lastSeenAt: json['last_seen_at'] != null 
          ? DateTime.parse(json['last_seen_at'] as String) 
          : DateTime.now(),
      createdAt: DateTime.parse(json['created_at'] as String),
      updatedAt: DateTime.parse(json['updated_at'] as String),
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }

  DeviceToken toEntity() {
    return DeviceToken(
      id: id,
      userId: userId,
      devicePlatform: devicePlatform,
      deviceLabel: deviceLabel,
      appRole: appRole,
      pushProviderName: pushProviderName,
      isActive: isActive,
      lastSeenAt: lastSeenAt,
      createdAt: createdAt,
      updatedAt: updatedAt,
    );
  }
}