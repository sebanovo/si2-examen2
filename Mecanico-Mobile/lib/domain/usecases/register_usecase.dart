import 'package:mechanic_mobile/domain/entities/user.dart';
import 'package:mechanic_mobile/domain/repositories/auth_repository.dart';

class RegisterUseCase {
  final AuthRepository repository;

  RegisterUseCase(this.repository);

  Future<User> call(Map<String, dynamic> body) {
    return repository.register(body);
  }
}
