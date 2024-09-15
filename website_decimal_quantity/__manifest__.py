{
    'name': "Website Decimal Quantity",
    'description': "Website Decimal",
    'version': "17.0.1.0",
    'application': True,
    'category': "Uncategorized",
    'summary': "website decimal quantity",
    'license': "LGPL-3",
    'author': "safa",
    'sequence': "1",
    'depends': [
        'web',
        'website_sale'
    ],
    'data': [
        # 'views/decimal_quantity_views.xml',
        #  'views/sale_order_line_views.xml',

    ],

    'assets': {
        'web.assets_frontend': [
            'website_decimal_quantity/static/src/js/decimal_quantity.js'
        ],

    }}
