# -*- coding: utf-8 -*-
{
    'name': "vendor_bill_from_reciept",

    'summary': "Create vendor bill from picking page (Receipts)",

    'description': """
Can create vendor bill from the picking page of purhcase Once the bill is created, the bill reference will be updated on picking record.
and provide a link on picking page to view the related bill
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase', 'account', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/create_bill_wizard_views.xml',
        'views/stock_picking_views.xml',
    ],
}

