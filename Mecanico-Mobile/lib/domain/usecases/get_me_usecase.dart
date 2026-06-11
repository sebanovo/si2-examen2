import 'package:mechanic_mobile/domain/entities/user.dart';
import 'package:mechanic_mobile/domain/repositories/auth_repository.dart';

class GetMeUseCase {
  final AuthRepository repository;

  GetMeUseCase(this.repository);

  Future<User> call() {
    return repository.getMe();
  }
}
