{
    'name':"Discount limit",
    'description': "Discount limit",
    'version': "17.0.1.0",
    'application': True,
    'category':"Uncategorized",
    'summary': "Discount limit",
    'license':"LGPL-3",
    'author': "safa",
    'sequence':"1",
    'depends': [
        'base',
        'sale'
],
'data': [
    'views/res_config_settings_views.xml',
    'views/sale_order_line_views.xml',
],
}
