import '../entities/user.dart';

abstract class AuthRepository {
  Future<User> login(String email, String password);
  Future<User> register(Map<String, dynamic> body);
  Future<User> getMe();
  Future<User> getMyProfile();
  Future<User> updateMyProfile(Map<String, dynamic> body);
}
