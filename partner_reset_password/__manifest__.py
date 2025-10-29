{
    'name': 'Reset Partner Password',
    'version': '18.0.0.0',
    'summary': "Reset user's password from partner form",
    'description': "This module allows administrators to reset a user's password directly from the partner form view. It adds a button that sends a password reset email to the associated user.",
    'author': 'Attefeh Falah',
    'website': 'https://www.techstarssolution.com',
    'category': 'Base',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/partner_reset_password_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}