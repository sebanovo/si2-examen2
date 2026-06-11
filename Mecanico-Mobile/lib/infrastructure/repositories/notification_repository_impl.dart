import '../../domain/entities/device_token.dart';
import '../../domain/usecases/register_device_usecase.dart';
import '../../domain/usecases/unregister_device_usecase.dart';
import '../../domain/usecases/get_my_devices_usecase.dart';
import '../datasources/notification_remote_data_source.dart';

class NotificationRepository {
  final NotificationRemoteDataSource _dataSource;

  NotificationRepository(this._dataSource);

  Future<DeviceToken> registerDevice(RegisterDeviceParams params) async {
    final model = await _dataSource.registerDevice(params.toJson());
    return model.toEntity();
  }

  Future<DeviceToken> unregisterDevice(String deviceTokenId) async {
    final model = await _dataSource.unregisterDevice(deviceTokenId);
    return model.toEntity();
  }

  Future<List<DeviceToken>> getMyDevices() async {
    final models = await _dataSource.getMyDevices();
    return models.map((model) => model.toEntity()).toList();
  }
}

// Implementación de UseCases
class RegisterDeviceUseCaseImpl implements RegisterDeviceUseCase {
  final NotificationRepository _repository;

  RegisterDeviceUseCaseImpl(this._repository);

  @override
  Future<DeviceToken> execute(RegisterDeviceParams params) async {
    return await _repository.registerDevice(params);
  }
}

class UnregisterDeviceUseCaseImpl implements UnregisterDeviceUseCase {
  final NotificationRepository _repository;

  UnregisterDeviceUseCaseImpl(this._repository);

  @override
  Future<DeviceToken> execute(String deviceTokenId) async {
    return await _repository.unregisterDevice(deviceTokenId);
  }
}

class GetMyDevicesUseCaseImpl implements GetMyDevicesUseCase {
  final NotificationRepository _repository;

  GetMyDevicesUseCaseImpl(this._repository);

  @override
  Future<List<DeviceToken>> execute() async {
    return await _repository.getMyDevices();
  }
}