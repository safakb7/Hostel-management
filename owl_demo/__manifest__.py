{
    'name':"owl demo",
    'description': "owl demo",
    'application': True,
    'depends':['base'],

'data': [
    'views/client_action.xml',
],
    'assets':{
        'web.assets_backend': [
            'owl_demo/static/src/**'
        ]
    }
}
