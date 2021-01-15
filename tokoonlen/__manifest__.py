{
    'name': 'tokoonlen',
    'version': '1.0',
    'description': 'toko',
    'summary': 'toko',
    'author': 'dhimas',
    'website': 'dhimas',
    'license': 'LGPL-3',
    'category': 'tokoonlen',
    'depends': [
        'base'
    ],
    'data': [
        'security/res_groups.xml',
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        'views/res_users_views.xml',
        'views/cabang_toko_views.xml',
        'views/transaksi_toko_views.xml',
        'views/transaksi_report_views.xml',
    ],
    'auto_install': True,
    'application': True,
}