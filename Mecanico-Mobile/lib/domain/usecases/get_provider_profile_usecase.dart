import '../entities/provider_profile.dart';

abstract class GetProviderProfileUseCase {
  Future<ProviderProfile> execute();
}
