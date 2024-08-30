{
    'name': 'Spanish Product Name',
    'version': '1.0',
    'installable': True,

    'depends': ['product', 'point_of_sale'
                ],
    'data': [
        'views/product_template_views.xml',
    ],

    'assets': {
        'point_of_sale._assets_pos': [
            'spanish_product_name/static/src/**/*',

        ],
    }

}
