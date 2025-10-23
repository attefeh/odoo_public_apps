{
    'name': 'ID Number Authentication',
    'version': '18.0.0.0',
    'summary': 'Enhance the signup process by adding ID number and extra fields.',
    'description': 'This module customizes the user signup process by incorporating an ID number field and additional fields to the signup form, improving user identification and data collection.',
    'author': 'Attefeh Falah',
    'website': 'https://www.techstarssolution.com',
    'category': 'Website',
    'depends': ['auth_signup'],
    'data': [
        'views/res_users_views.xml',
        'views/res_partner_views.xml',
        'views/auth_signup_login_templates.xml',
        'views/webclient_template.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}