import 'package:flutter/material.dart';
import '../../domain/entities/provider_summary.dart';
import '../../domain/usecases/get_providers_usecase.dart';

class AdminProvidersViewModel extends ChangeNotifier {
  final GetProvidersUseCase _getProvidersUseCase;

  List<ProviderSummary> _providers = [];
  bool _isLoading = false;
  String? _errorMessage;
  String _filterType = 'all'; // all, workshop, independent

  AdminProvidersViewModel({required GetProvidersUseCase getProvidersUseCase})
    : _getProvidersUseCase = getProvidersUseCase;

  List<ProviderSummary> get providers => _providers;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;
  String get filterType => _filterType;

  List<ProviderSummary> get filteredProviders {
    if (_filterType == 'all') return _providers;
    if (_filterType == 'workshop') {
      return _providers.where((p) => p.providerType == 'WORKSHOP').toList();
    }
    if (_filterType == 'independent') {
      return _providers
          .where((p) => p.providerType == 'INDEPENDENT_MECHANIC')
          .toList();
    }
    return _providers;
  }

  Future<void> loadProviders({int limit = 50, int offset = 0}) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _providers = await _getProvidersUseCase.execute(
        limit: limit,
        offset: offset,
      );
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  void setFilterType(String filter) {
    _filterType = filter;
    notifyListeners();
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
