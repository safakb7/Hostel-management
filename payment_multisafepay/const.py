SUPPORTED_CURRENCIES = [
    'AUD',
    'CAD',
    'CHF',
    'DKK',
    'USD',

]

DEFAULT_PAYMENT_METHODS_CODES = [
    # Primary payment methods.
    'card',
    'ideal',
    # Brand payment methods.
    'visa',
    'mastercard',
    'amex',
    'discover',
]

# Mapping of payment method codes to Multisafepay codes.
PAYMENT_METHODS_MAPPING = {
    'apple_pay': 'applepay',
    'card': 'creditcard',
    'bank_transfer': 'banktransfer',
    'kbc_cbc': 'kbc',
    'p24': 'przelewy24',
    'sepa_direct_debit': 'directdebit',
}