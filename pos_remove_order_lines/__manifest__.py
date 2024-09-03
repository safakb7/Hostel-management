{
    'name':"Pos Remove Order Lines",
    'description': "Remove Order Lines",
    'version': "17.0.1.0",
    'application': True,
    'category':"Uncategorized",
    'summary': "Pos remove order lines",
    'license':"LGPL-3",
    'author': "safa",
    'sequence':"1",
    'depends': [
        'base',
        'point_of_sale'
    ],

    'assets': {
        'point_of_sale._assets_pos': [
            'pos_remove_order_lines/static/src/**/*',
        ],
    }
}
