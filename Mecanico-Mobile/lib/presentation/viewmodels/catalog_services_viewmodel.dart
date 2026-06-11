import 'package:flutter/material.dart';
import '../../domain/entities/catalog_service.dart';
import '../../domain/usecases/get_catalog_services_usecase.dart';
import '../../domain/usecases/get_provider_services_usecase.dart';
import '../../domain/usecases/create_provider_service_usecase.dart';

class CatalogServicesViewModel extends ChangeNotifier {
  final GetCatalogServicesUseCase _getCatalogServicesUseCase;
  final GetProviderServicesUseCase _getProviderServicesUseCase;
  final CreateProviderServiceUseCase _createProviderServiceUseCase;

  List<CatalogServiceEntry> _catalogServices = [];
  List<ProviderService> _providerServices = [];
  bool _isLoading = false;
  String? _errorMessage;

  CatalogServicesViewModel({
    required GetCatalogServicesUseCase getCatalogServicesUseCase,
    required GetProviderServicesUseCase getProviderServicesUseCase,
    required CreateProviderServiceUseCase createProviderServiceUseCase,
  }) : _getCatalogServicesUseCase = getCatalogServicesUseCase,
       _getProviderServicesUseCase = getProviderServicesUseCase,
       _createProviderServiceUseCase = createProviderServiceUseCase;

  List<CatalogServiceEntry> get catalogServices => _catalogServices;
  List<ProviderService> get providerServices => _providerServices;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  Future<void> loadCatalogServices() async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _catalogServices = await _getCatalogServicesUseCase.execute();
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<void> loadProviderServices() async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _providerServices = await _getProviderServicesUseCase.execute();
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<bool> createProviderService({
    required String serviceCatalogItemId,
    String? customTitle,
    String? customDescription,
    required double priceEstimateMin,
    required double priceEstimateMax,
    required int estimatedDurationMinutes,
    required bool isMobileServiceEnabled,
    required bool isEmergencyServiceEnabled,
    required bool isActive,
  }) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final params = CreateProviderServiceParams(
        serviceCatalogItemId: serviceCatalogItemId,
        customTitle: customTitle,
        customDescription: customDescription,
        priceEstimateMin: priceEstimateMin,
        priceEstimateMax: priceEstimateMax,
        estimatedDurationMinutes: estimatedDurationMinutes,
        isMobileServiceEnabled: isMobileServiceEnabled,
        isEmergencyServiceEnabled: isEmergencyServiceEnabled,
        isActive: isActive,
      );

      final newService = await _createProviderServiceUseCase.execute(params);
      _providerServices.add(newService);

      // Actualizar también el catalog service
      final index = _catalogServices.indexWhere(
        (s) => s.catalogItem.id == serviceCatalogItemId,
      );
      if (index != -1) {
        _catalogServices[index] = CatalogServiceEntry(
          catalogItem: _catalogServices[index].catalogItem,
          providerService: newService,
          isConfigured: true,
        );
      }

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

  bool isServiceConfigured(String catalogItemId) {
    return _catalogServices.any(
      (s) => s.catalogItem.id == catalogItemId && s.isConfigured,
    );
  }

  ProviderService? getProviderService(String catalogItemId) {
    final entry = _catalogServices.firstWhere(
      (s) => s.catalogItem.id == catalogItemId,
      orElse: () => CatalogServiceEntry(
        catalogItem: CatalogItem(
          id: '',
          code: '',
          category: '',
          title: '',
          description: '',
          supportsMobileService: false,
          supportsEmergencyService: false,
          isActive: false,
          sortOrder: 0,
          createdAt: DateTime.now(),
          updatedAt: DateTime.now(),
        ),
        isConfigured: false,
      ),
    );
    return entry.providerService;
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
