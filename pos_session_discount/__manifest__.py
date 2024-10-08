{
    'name':"Pos Session Discount",
    'description': "Pos Session Discount",
    'version': "17.0.1.0",
    'application': True,
    'category':"Uncategorized",
    'summary': "Pos discount",
    'license':"LGPL-3",
    'author': "safa",
    'sequence':"1",
    'depends': [
        'base',
        'point_of_sale'
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'views/pos_order_line_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_session_discount/static/src/**/*',
        ],
    }
}
