import 'package:dio/dio.dart';
import 'package:http_parser/http_parser.dart';
import '../../constants/env.dart';

class ApiClient {
  late final Dio dio;
  String? token;

  ApiClient() {
    dio = Dio(
      BaseOptions(
        baseUrl: Env.baseUrl,
        connectTimeout: const Duration(seconds: 30),
        receiveTimeout: const Duration(seconds: 30),
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
        },
      ),
    );

    // Interceptor para agregar token automáticamente
    dio.interceptors.add(
      InterceptorsWrapper(
        onRequest: (options, handler) {
          if (token != null) {
            options.headers["Authorization"] = "Bearer $token";
          }
          if (options.data != null) {}
          return handler.next(options);
        },
        onResponse: (response, handler) {
          return handler.next(response);
        },
        onError: (error, handler) {
          return handler.next(error);
        },
      ),
    );
  }

  void setToken(String token) {
    this.token = token;
  }

  void clearToken() {
    token = null;
  }

  Future<Response> post(String path, dynamic data) async {
    return await dio.post(path, data: data);
  }

  Future<Response> get(String path) async {
    return await dio.get(path);
  }

  Future<Response> patch(String path, dynamic data) async {
    return await dio.patch(path, data: data);
  }

  Future<Response> delete(String path) async {
    return await dio.delete(path);
  }

  Future<Response> uploadFile(
    String path, {
    required String fieldName,
    required String fileName,
    required List<int> bytes,
    required String mimeType,
    Map<String, dynamic>? additionalFields,
  }) async {
    final formData = FormData();

    // Agregar campos adicionales como texto
    if (additionalFields != null) {
      additionalFields.forEach((key, value) {
        formData.fields.add(MapEntry(key, value.toString()));
      });
    }

    // Agregar el archivo
    final multipartFile = MultipartFile.fromBytes(
      bytes,
      filename: fileName,
      contentType: MediaType.parse(mimeType),
    );
    formData.files.add(MapEntry(fieldName, multipartFile));

    return await dio.post(
      path,
      data: formData,
      options: Options(headers: {"Content-Type": "multipart/form-data"}),
    );
  }
}
