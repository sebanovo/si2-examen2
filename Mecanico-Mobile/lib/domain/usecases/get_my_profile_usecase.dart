import 'package:mechanic_mobile/domain/entities/user.dart';
import 'package:mechanic_mobile/domain/repositories/auth_repository.dart';

class GetMyProfileUseCase {
  final AuthRepository repository;

  GetMyProfileUseCase(this.repository);

  Future<User> call() {
    return repository.getMyProfile();
  }
}
