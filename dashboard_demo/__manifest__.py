{
    'name':"dashboard demo",
    'description': "dashboard demo",
    'application': True,
    'depends':['base'],

'data': [
    'views/new_dashboard.xml',
],
    'assets':{
        'web.assets_backend': [
            'dashboard_demo/static/src/**'
        ]
    }
}
