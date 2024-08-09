{
    'name':"Employee Transfer",
    'description': "employee transfer",
    'application': True,
    'summary': "employee transfer",
    'author': "safa",
    'sequence':"1",
    'depends': [
        'base',
        'hr'

    ],

'data': [
    'views/company_transfer_views.xml',
    'views/manager_approve_views.xml',

    'security/ir.model.access.csv',



],
}
