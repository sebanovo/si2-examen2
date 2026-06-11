import 'package:mechanic_mobile/domain/entities/device_token.dart';

abstract class UnregisterDeviceUseCase {
  Future<DeviceToken> execute(String deviceTokenId);
}
