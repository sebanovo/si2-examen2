import 'package:flutter/foundation.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:mechanic_mobile/core/di/injection_container.dart';
import '../../domain/usecases/register_device_usecase.dart';
import '../../domain/usecases/unregister_device_usecase.dart';
import '../../domain/usecases/get_my_devices_usecase.dart';

class NotificationService {
  final FirebaseMessaging _firebaseMessaging = FirebaseMessaging.instance;
  String? _currentDeviceToken;

  static final NotificationService _instance = NotificationService._internal();
  factory NotificationService() => _instance;
  NotificationService._internal();

  Future<void> initialize() async {
    // Solicitar permisos
    await _requestPermissions();

    // Obtener token FCM
    await _getToken();

    // Escuchar mensajes en primer plano
    FirebaseMessaging.onMessage.listen(_handleForegroundMessage);

    // Escuchar cuando se abre la app desde notificación
    FirebaseMessaging.onMessageOpenedApp.listen(_handleMessageOpenedApp);

    // Manejar mensaje inicial si la app se abrió desde una notificación
    final initialMessage = await FirebaseMessaging.instance.getInitialMessage();
    if (initialMessage != null) {
      _handleMessageOpenedApp(initialMessage);
    }
  }

  Future<void> _requestPermissions() async {
    if (kIsWeb) {
      // Web: solicitar permisos
      await _firebaseMessaging.requestPermission();
    } else {
      // Móvil: solicitar permisos
      NotificationSettings settings = await _firebaseMessaging
          .requestPermission(alert: true, badge: true, sound: true);
      debugPrint('📱 Notification permission: ${settings.authorizationStatus}');
    }
  }

  Future<void> _getToken() async {
    try {
      _currentDeviceToken = await _firebaseMessaging.getToken();
      debugPrint('📱 FCM Token: $_currentDeviceToken');

      if (_currentDeviceToken != null) {
        // Registrar el dispositivo automáticamente
        await registerCurrentDevice();
      }
    } catch (e) {
      debugPrint('❌ Error getting FCM token: $e');
    }
  }

  Future<void> registerCurrentDevice() async {
    if (_currentDeviceToken == null) return;

    try {
      final registerUseCase = sl<RegisterDeviceUseCase>();

      // Determinar plataforma
      String platform;
      if (kIsWeb) {
        platform = 'WEB';
      } else if (defaultTargetPlatform == TargetPlatform.iOS) {
        platform = 'IOS';
      } else {
        platform = 'ANDROID';
      }

      final params = RegisterDeviceParams(
        deviceToken: _currentDeviceToken!,
        devicePlatform: platform,
        deviceLabel: null,
        appRole: 'CLIENT', // O el rol actual del usuario
      );

      await registerUseCase.execute(params);
      debugPrint('✅ Device registered successfully');
    } catch (e) {
      debugPrint('❌ Error registering device: $e');
    }
  }

  Future<void> unregisterCurrentDevice() async {
    if (_currentDeviceToken == null) return;

    try {
      final getDevicesUseCase = sl<GetMyDevicesUseCase>();
      final devices = await getDevicesUseCase.execute();

      final device = devices.firstWhere(
        (d) =>
            d.devicePlatform ==
            (kIsWeb
                ? 'WEB'
                : (defaultTargetPlatform == TargetPlatform.iOS
                      ? 'IOS'
                      : 'ANDROID')),
        orElse: () => throw Exception('Device not found'),
      );

      final unregisterUseCase = sl<UnregisterDeviceUseCase>();
      await unregisterUseCase.execute(device.id);
      debugPrint('✅ Device unregistered successfully');
    } catch (e) {
      debugPrint('❌ Error unregistering device: $e');
    }
  }

  void _handleForegroundMessage(RemoteMessage message) {
    debugPrint(
      '📨 Message received in foreground: ${message.notification?.title}',
    );
    // Aquí puedes mostrar una notificación local o actualizar la UI
  }

  void _handleMessageOpenedApp(RemoteMessage message) {
    debugPrint(
      '📨 App opened from notification: ${message.notification?.title}',
    );
    // Aquí puedes navegar a la pantalla correspondiente
  }

  Future<void> subscribeToTopic(String topic) async {
    await _firebaseMessaging.subscribeToTopic(topic);
    debugPrint('✅ Subscribed to topic: $topic');
  }

  Future<void> unsubscribeFromTopic(String topic) async {
    await _firebaseMessaging.unsubscribeFromTopic(topic);
    debugPrint('✅ Unsubscribed from topic: $topic');
  }

  String? get currentToken => _currentDeviceToken;
}
