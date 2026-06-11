import '../entities/device_token.dart';

abstract class RegisterDeviceUseCase {
  Future<DeviceToken> execute(RegisterDeviceParams params);
}

class RegisterDeviceParams {
  final String deviceToken;
  final String devicePlatform; // ANDROID, IOS, WEB
  final String? deviceLabel;
  final String appRole;

  RegisterDeviceParams({
    required this.deviceToken,
    required this.devicePlatform,
    this.deviceLabel,
    required this.appRole,
  });

  Map<String, dynamic> toJson() => {
    'device_token': deviceToken,
    'device_platform': devicePlatform,
    if (deviceLabel != null) 'device_label': deviceLabel,
    'app_role': appRole,
  };
}
