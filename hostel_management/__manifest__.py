{
    'name': "Hostel Management",
    'description': "Hostel",
    'version': "17.0.1.0",
    'application': True,
    'category': "Uncategorized",
    'summary': "Hostel Management",
    'license': "LGPL-3",
    'author': "safa",
    'sequence': "5",
    'depends':
        [
            'web',
            'mail',
            'product',
            'sale',
            'account',
            'base_automation',
            'website',
        ],
    'data': [
        'security/user_group.xml',
        'security/ir.model.access.csv',

        'views/hostel_room_views.xml',
        'views/hostel_student_views.xml',
        'views/hostel_facilities_views.xml',
        'views/leave_request_views.xml',
        'views/student_invoice_views.xml',
        'views/cleaning_service_views.xml',

        'data/room_sequence.xml',
        'data/student_sequence.xml',
        'data/demo_data.xml',
        'data/product_data.xml',
        'data/email_template.xml',
        'data/invoice_data.xml',
        'data/user_automation.xml',
        'data/ir_rule.xml',

        'report/student_template.xml',
        'report/student_report.xml',
        'report/leave_request_template.xml',

        'report/leave_request_report.xml',

        'views/hostel_report_menu.xml',
        'wizard/student_wizard_views.xml',

        'wizard/leave_request_wizard_views.xml',
        'views/student_register_template.xml',
        'views/thankyou_message.xml',
        'views/available_room_template.xml',
        'views/student_register_views.xml',

        'views/available_room_views.xml',
        'views/room_snippet.xml',
        'views/room_data_template.xml',

    ],
    'css': ['hostel_management/static/src/css/style.css'],
    'assets': {
        'web.assets_backend': [
            'hostel_management/static/src/js/action_manager.js',

        ],
        'web.assets_frontend': [
            'hostel_management/static/src/js/snippet.js',
             'hostel_management/static/src/xml/latest_room_template.xml',

        ],
    }}
