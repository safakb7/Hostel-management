{
    'name': "Range Slider",
    'description': "Range slider",
    'version': "17.0.1.0",
    'application': True,
    'category': "Uncategorized",
    'summary': "range slider field widget",
    'license': "LGPL-3",
    'author': "safa",
    'sequence': "1",
    'depends': [
        'base', 'web',
    ],
    'data': [
        'views/res_partner_views.xml'
      ],

    'assets': {
        'web.assets_backend': [
            'range_slider/static/src/**/*',
        ],
}}
