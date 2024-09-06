{
    'name': 'Multisafepay Payment',
    'version': '1.0',
    'category': 'Accounting/Payment Providers',
    'sequence': 1,
    'summary': "A Dutch payment provider covering several European countries.",
    'description': " ",  # Non-empty string to avoid loading the README file.
    'author': 'safa',
    'website': '',
    'depends': ['payment'],
    'data': [
        'views/payment_provider.xml',
        'views/payment_multisafepay_template.xml',
        'data/payment_method_data.xml',

        'data/payment_provider_data.xml',


    ],
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3'
}
