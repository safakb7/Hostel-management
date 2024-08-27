{
    'name':"Ecommerce Clear Cart",
    'description': "Clear Cart",
    'version': "17.0.1.0",
    'application': True,
    'category':"Uncategorized",
    'summary': "ecommerce clear cart",
    'license':"LGPL-3",
    'author': "safa",
    'sequence':"1",
    'depends': [
        'web',
        'website_sale'
],
'data': [
    'views/clear_cart_views.xml'

],
    'assets': {
        'web.assets_frontend': [
            'ecommerce_clear_cart/static/src/js/clear_cart.js'
        ],

}}
