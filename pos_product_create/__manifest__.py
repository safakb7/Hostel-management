{
    'name':"Pos Product Create",
    'description': "Pos Product Create",
    'version': "17.0.1.0",
    'application': True,
    'category':"Uncategorized",
    'summary': "Pos product create and edit",
    'license':"LGPL-3",
    'author': "safa",
    'sequence':"1",
    'depends': [
        'base',
        'point_of_sale'
    ],
    'data': [

    ],
     'assets': {
        'point_of_sale._assets_pos': [
            'pos_product_create/static/src/**/*',
        ],
    }
}
