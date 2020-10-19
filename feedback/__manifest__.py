# -*- coding: utf-8 -*-
{
    'name': "Feedback",

    'summary': """
        My awesome feedback module""",

    'description': """
        My awesome feedback module
    """,

    'author': "Mars & co",
    'website': "http://www.marsik.ru",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'useful',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
