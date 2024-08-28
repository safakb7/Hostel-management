{
    'name': 'Spanish Product Name',
    'version': '1.0',
    'installable': True,

    'depends': ['product'
                ],
    'data': [
        'views/product_template_views.xml',
        'views/pos_receipt_views.xml'
    ],

    'assets': {
        'point_of_sale.assets': [
            'spanish_product_name/static/src/js/pos_receipt.js',
        ],
    }

}
