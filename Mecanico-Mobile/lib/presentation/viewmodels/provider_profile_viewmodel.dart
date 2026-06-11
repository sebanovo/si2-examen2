import 'package:flutter/material.dart';
import '../../domain/entities/provider_profile.dart';
import '../../domain/usecases/get_provider_profile_usecase.dart';
import '../../domain/usecases/update_provider_profile_usecase.dart';

class ProviderProfileViewModel extends ChangeNotifier {
  final GetProviderProfileUseCase _getProviderProfileUseCase;
  final UpdateProviderProfileUseCase _updateProviderProfileUseCase;

  ProviderProfile? _profile;
  bool _isLoading = false;
  String? _errorMessage;

  ProviderProfileViewModel({
    required GetProviderProfileUseCase getProviderProfileUseCase,
    required UpdateProviderProfileUseCase updateProviderProfileUseCase,
  }) : _getProviderProfileUseCase = getProviderProfileUseCase,
       _updateProviderProfileUseCase = updateProviderProfileUseCase;

  ProviderProfile? get profile => _profile;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  Future<void> loadProfile() async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _profile = await _getProviderProfileUseCase.execute();
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<bool> updateProfile({
    String? businessName,
    String? legalName,
    String? description,
    String? contactEmail,
    String? contactPhone,
    String? city,
    String? address,
    double? baseLatitude,
    double? baseLongitude,
    bool? isAvailable,
    int? maxConcurrentServices,
  }) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final params = UpdateProviderProfileParams(
        businessName: businessName,
        legalName: legalName,
        description: description,
        contactEmail: contactEmail,
        contactPhone: contactPhone,
        city: city,
        address: address,
        baseLatitude: baseLatitude,
        baseLongitude: baseLongitude,
        isAvailable: isAvailable,
        maxConcurrentServices: maxConcurrentServices,
      );

      _profile = await _updateProviderProfileUseCase.execute(params);
      notifyListeners();
      return true;
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
      return false;
    } finally {
      _setLoading(false);
    }
  }

  Future<bool> toggleAvailability() async {
    if (_profile == null) return false;
    return await updateProfile(isAvailable: !_profile!.isAvailable);
  }

  void _setLoading(bool loading) {
    _isLoading = loading;
    notifyListeners();
  }

  void clearError() {
    _errorMessage = null;
    notifyListeners();
  }
}
