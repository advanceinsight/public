# -*- coding: utf-8 -*-
{
    'name': "MGA Customisation",
    'summary': """This module is used to add small customisations to the MGA Odoo database without creating a separate module.""",
    'description': """This module is used to add small customisations to the MGA Odoo database without creating a separate module.""",
    'author': "Advance Insight",
    'website': "http://advanceinsight.dev",
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'timesheet_grid'
        ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/inherited_views.xml',
    ],
}
