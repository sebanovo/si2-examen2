import '../entities/provider_profile.dart';

abstract class UpdateProviderProfileUseCase {
  Future<ProviderProfile> execute(UpdateProviderProfileParams params);
}

class UpdateProviderProfileParams {
  final String? businessName;
  final String? legalName;
  final String? description;
  final String? contactEmail;
  final String? contactPhone;
  final String? city;
  final String? address;
  final double? baseLatitude;
  final double? baseLongitude;
  final bool? isAvailable;
  final int? maxConcurrentServices;

  UpdateProviderProfileParams({
    this.businessName,
    this.legalName,
    this.description,
    this.contactEmail,
    this.contactPhone,
    this.city,
    this.address,
    this.baseLatitude,
    this.baseLongitude,
    this.isAvailable,
    this.maxConcurrentServices,
  });

  Map<String, dynamic> toJson() => {
    if (businessName != null) 'business_name': businessName,
    if (legalName != null) 'legal_name': legalName,
    if (description != null) 'description': description,
    if (contactEmail != null) 'contact_email': contactEmail,
    if (contactPhone != null) 'contact_phone': contactPhone,
    if (city != null) 'city': city,
    if (address != null) 'address': address,
    if (baseLatitude != null) 'base_latitude': baseLatitude,
    if (baseLongitude != null) 'base_longitude': baseLongitude,
    if (isAvailable != null) 'is_available': isAvailable,
    if (maxConcurrentServices != null)
      'max_concurrent_services': maxConcurrentServices,
  };
}
