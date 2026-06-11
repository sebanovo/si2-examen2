import '../entities/device_token.dart';

abstract class GetMyDevicesUseCase {
  Future<List<DeviceToken>> execute();
}
