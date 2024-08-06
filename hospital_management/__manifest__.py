{
    'name':"Hospital Management",

    'depends':[
        'base',
        'hr',
        'hr_hourly_cost'

    ],
    'data':[

    'views/specialization_tag.xml',
    'views/hospital_op_views.xml',
    'views/hospital_op_menus.xml',

        'views/hospital_patient_menus.xml',
        'views/hospital_views.xml',

        'views/hospital_doctor_menus.xml',
        'views/hospital_doctor_views.xml',
        'views/my_module_sequence.xml',
        'security/ir.model.access.csv',

    ],
}