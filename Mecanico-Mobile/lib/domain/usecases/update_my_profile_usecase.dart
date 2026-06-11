import 'package:mechanic_mobile/domain/entities/user.dart';
import 'package:mechanic_mobile/domain/repositories/auth_repository.dart';

class UpdateMyProfileUseCase {
  final AuthRepository repository;

  UpdateMyProfileUseCase(this.repository);

  Future<User> call({
    required String firstName,
    required String lastName,
    required String phoneNumber,
  }) {
    return repository.updateMyProfile({
      "first_name": firstName,
      "last_name": lastName,
      "phone_number": phoneNumber,
    });
  }
}
