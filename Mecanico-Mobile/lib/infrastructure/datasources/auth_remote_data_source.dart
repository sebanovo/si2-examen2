import 'package:dio/dio.dart';
import '../models/user_model.dart';
import '../../core/network/api_client.dart';

class AuthRemoteDataSource {
  final ApiClient api;

  AuthRemoteDataSource(this.api);

  // Helper para extraer mensaje de error de la respuesta
  String _extractErrorMessage(dynamic responseData) {
    if (responseData is Map<String, dynamic>) {
      if (responseData['message'] != null) return responseData['message'];
      if (responseData['error'] != null &&
          responseData['error']['message'] != null) {
        return responseData['error']['message'];
      }
    }
    return 'Error desconocido';
  }

  Future<(String, UserModel)> login(String email, String password) async {
    try {
      final response = await api.post("/api/auth/login", {
        "email": email,
        "password": password,
      });

      final Map<String, dynamic> jsonResponse = response.data;
      if (jsonResponse['success'] == true) {
        final data = jsonResponse['data'];
        final String token = data["access_token"] ?? "";
        final Map<String, dynamic> userJson =
            (data["user"] as Map<String, dynamic>?) ??
            data as Map<String, dynamic>;
        final user = UserModel.fromJson(userJson);
        return (token, user);
      } else {
        throw Exception(_extractErrorMessage(jsonResponse));
      }
    } on DioException catch (e) {
      if (e.response != null && e.response?.data != null) {
        throw Exception(_extractErrorMessage(e.response?.data));
      }
      throw Exception('Error de conexión: ${e.message}');
    }
  }

  Future<(String, UserModel)> register(Map<String, dynamic> body) async {
    try {
      final response = await api.post("/api/auth/register", body);
      final Map<String, dynamic> jsonResponse = response.data;
      if (jsonResponse['success'] == true) {
        final data = jsonResponse['data'];
        final String token = data["access_token"] ?? "";
        final Map<String, dynamic> userJson =
            (data["user"] as Map<String, dynamic>?) ??
            data as Map<String, dynamic>;
        final user = UserModel.fromJson(userJson);
        return (token, user);
      } else {
        throw Exception(_extractErrorMessage(jsonResponse));
      }
    } on DioException catch (e) {
      if (e.response != null && e.response?.data != null) {
        throw Exception(_extractErrorMessage(e.response?.data));
      }
      throw Exception('Error de conexión: ${e.message}');
    }
  }

  Future<UserModel> me() async {
    try {
      final response = await api.get("/api/auth/me");
      final Map<String, dynamic> jsonResponse = response.data;
      if (jsonResponse['success'] == true) {
        return UserModel.fromJson(jsonResponse['data']);
      } else {
        throw Exception(_extractErrorMessage(jsonResponse));
      }
    } on DioException catch (e) {
      if (e.response != null && e.response?.data != null) {
        throw Exception(_extractErrorMessage(e.response?.data));
      }
      throw Exception('Error de conexión: ${e.message}');
    }
  }

  Future<UserModel> myProfile() async {
    try {
      final response = await api.get("/api/users/me/profile");
      final Map<String, dynamic> jsonResponse = response.data;
      if (jsonResponse['success'] == true) {
        return UserModel.fromJson(jsonResponse['data']);
      } else {
        throw Exception(_extractErrorMessage(jsonResponse));
      }
    } on DioException catch (e) {
      if (e.response != null && e.response?.data != null) {
        throw Exception(_extractErrorMessage(e.response?.data));
      }
      throw Exception('Error de conexión: ${e.message}');
    }
  }

  Future<UserModel> updateMyProfile(Map<String, dynamic> body) async {
    try {
      final response = await api.patch("/api/users/me/profile", body);
      final Map<String, dynamic> jsonResponse = response.data;
      if (jsonResponse['success'] == true) {
        return UserModel.fromJson(jsonResponse['data']);
      } else {
        throw Exception(_extractErrorMessage(jsonResponse));
      }
    } on DioException catch (e) {
      if (e.response != null && e.response?.data != null) {
        throw Exception(_extractErrorMessage(e.response?.data));
      }
      throw Exception('Error de conexión: ${e.message}');
    }
  }
}
