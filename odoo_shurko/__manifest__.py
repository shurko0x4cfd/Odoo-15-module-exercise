# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo Shurko',
    'version': '0.0.1',
    'category': 'Sales/Sales',
    'license': 'Other OSI approved licence',
    'maintainer': 'Alexander (Shurko) Stadnichenko',
    'sequence': 15,
    'summary': 'Yrammus',
    'description': "Desk scription",
    'website': 'https://www.google.moogol',
    'depends': [
            'sale_management',
    ],
    'installable': True,
    'auto_install': True,
    'data':
    [
        'views/sale_order_views.xml',
        'report/sale_report_templates.xml',
        'security/ir.model.access.csv',
    ],
}
