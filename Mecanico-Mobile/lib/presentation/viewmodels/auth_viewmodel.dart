import 'package:flutter/material.dart';
import '../../domain/usecases/login_usecase.dart';
import '../../domain/usecases/register_usecase.dart';
import '../../domain/usecases/get_me_usecase.dart';
import '../../domain/usecases/get_my_profile_usecase.dart';
import '../../domain/usecases/update_my_profile_usecase.dart';
import '../../domain/entities/user.dart';

class AuthViewModel extends ChangeNotifier {
  final LoginUseCase loginUseCase;
  final RegisterUseCase registerUseCase;
  final GetMeUseCase getMeUseCase;
  final GetMyProfileUseCase getMyProfileUseCase;
  final UpdateMyProfileUseCase updateMyProfileUseCase;

  User? user;
  bool isLoading = false;
  String? errorMessage;

  AuthViewModel(
    this.loginUseCase,
    this.registerUseCase,
    this.getMeUseCase,
    this.getMyProfileUseCase,
    this.updateMyProfileUseCase,
  );

  void logout() {
    user = null;
    // Aquí también podrías limpiar el token del ApiClient si es necesario
    notifyListeners();
  }

  Future<bool> login(String email, String password) async {
    isLoading = true;
    errorMessage = null;
    notifyListeners();

    try {
      user = await loginUseCase(email, password);
      return true; // ✅ éxito
    } catch (e) {
      errorMessage = e.toString(); // ✅ capturas error
      return false;
    } finally {
      isLoading = false;
      notifyListeners();
    }
  }

  Future<bool> register(Map<String, dynamic> body) async {
    isLoading = true;
    errorMessage = null;
    notifyListeners();

    try {
      user = await registerUseCase(body);
      return true;
    } catch (e) {
      errorMessage = e.toString();
      return false;
    } finally {
      isLoading = false;
      notifyListeners();
    }
  }

  Future<void> loadMe() async {
    try {
      user = await getMeUseCase();
      notifyListeners();
    } catch (e) {
      errorMessage = e.toString();
      notifyListeners();
    }
  }

  Future<void> loadMyProfile() async {
    try {
      user = await getMyProfileUseCase();
      notifyListeners();
    } catch (e) {
      errorMessage = e.toString();
      notifyListeners();
    }
  }

  Future<bool> updateMyProfile({
    required String firstName,
    required String lastName,
    required String phoneNumber,
  }) async {
    isLoading = true;
    errorMessage = null;
    notifyListeners();

    try {
      user = await updateMyProfileUseCase(
        firstName: firstName,
        lastName: lastName,
        phoneNumber: phoneNumber,
      );
      return true;
    } catch (e) {
      errorMessage = e.toString();
      return false;
    } finally {
      isLoading = false;
      notifyListeners();
    }
  }
}
