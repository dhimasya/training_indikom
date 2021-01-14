from odoo import http
from odoo.http import route, request
import json

class Buku(http.Controller):

    @route('/perpus/list_buku', type='http', auth='none', methods=['POST'], csrf=False)
    def perpus_list_buku(self, **params):
        # kalau misal data tidak ada di params
        # cek di request.httprequest.data
        print(request.httprequest.data, params)
        data = []
        domain = []
        request_body = json.loads(request.httprequest.data or '{}')
        judul = request_body.get('judul')
        if judul:
            domain.append(['name', 'ilike', judul])
        rows = request.env['buku'].sudo().search(domain)
        # request.cr.execute('')
        # res_cr = request.cr.fetchall()
        for row in rows:
            data.append({
                'judul': row.name,
                'deskripsi': row.deskripsi,
                'kategori': row.kategori_id.name,
                'halaman': row.halaman,
            })
        return request.make_response(json.dumps({
            'success': True,
            'message': '',
            'data': data
        }))
    
    @route('/perpus/testing', type='http', auth='none')
    def perpus_testing(self, **params):
        data = json.loads(request.httprequest.data)
        return request.make_response(json.dumps({'userku': data.get('user')}))
