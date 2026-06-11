class DeviceToken {
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

  DeviceToken({
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

  String get platformIcon {
    switch (devicePlatform.toUpperCase()) {
      case 'ANDROID':
        return '🤖';
      case 'IOS':
        return '📱';
      case 'WEB':
        return '🌐';
      default:
        return '💻';
    }
  }

  String get statusText => isActive ? 'Activo' : 'Inactivo';
}
