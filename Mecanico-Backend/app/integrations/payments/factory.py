from app.integrations.payments.base import PaymentProvider
from app.integrations.payments.mock_provider import MockPaymentProvider


def get_payment_provider() -> PaymentProvider:
    """
    Factory centralizada para proveedores de pago.

    Por ahora se usa MockPaymentProvider porque el examen necesita demostrar el flujo
    completo sin procesar dinero real. Más adelante puede reemplazarse por Stripe,
    QR bancario, pasarela local u otro proveedor.
    """

    return MockPaymentProvider()