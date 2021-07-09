{
    'name': 'purchase_discount',
    'version': '0.1',
    'Category': 'Tools',
    'Summary': 'adding a discount field to existing purchase module',
    'depends': ['purchase'],
    'data': ['views/dis_order_line.xml',
             'views/dis_order_tree.xml',
             'views/invoice_view.xml',
             'views/move_line.xml',
             'report/report_order_purchase.xml'],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True
}