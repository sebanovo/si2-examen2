import '../../domain/entities/user.dart';
import '../../domain/repositories/auth_repository.dart';
import '../datasources/auth_remote_data_source.dart';
import '../../core/network/api_client.dart';

class AuthRepositoryImpl implements AuthRepository {
  final AuthRemoteDataSource remote;
  final ApiClient api;

  AuthRepositoryImpl(this.remote, this.api);

  @override
  Future<User> login(String email, String password) async {
    final (token, user) = await remote.login(email, password);
    api.setToken(token);
    return user;
  }

  @override
  Future<User> register(Map<String, dynamic> body) async {
    final (token, user) = await remote.register(body);
    api.setToken(token);
    return user;
  }

  // ✅ Implementar getMe
  @override
  Future<User> getMe() async {
    return await remote.me();
  }

  @override
  Future<User> getMyProfile() async {
    return await remote.myProfile();
  }

  @override
  Future<User> updateMyProfile(Map<String, dynamic> body) async {
    return await remote.updateMyProfile(body);
  }
}
