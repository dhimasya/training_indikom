{
    'name': 'Perpus',
    'version': '1.0',
    'description': 'module perpustakaan',
    'summary': 'module perpustakaan',
    'author': 'author',
    'website': 'website',
    'license': 'LGPL-3',
    'category': 'Perpus',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/buku_views.xml',
        'views/anggota_views.xml',
        'views/transaksi_views.xml',
        'views/kategori_buku_views.xml',
        'wizard/buku_kembali_views.xml',
        'report/buku_report.xml',
        'views/assets_backend.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'auto_install': True,
    'application': True,
}