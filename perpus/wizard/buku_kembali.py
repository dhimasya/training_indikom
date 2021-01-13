# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import UserError

class BukuKembali(models.TransientModel):
    _name = 'buku.kembali'
    _description = 'wizard buku kembali'

    transaksi_ids = fields.Many2many('transaksi')
    tanggal_kembali = fields.Date(required=True)

    def default_get(self, fields_list):
        res = super(BukuKembali, self).default_get(fields_list)
        transaksi_ids = self._context.get('active_ids')
        transaksis = self.env['transaksi'].browse(transaksi_ids)
        if not transaksis:
            raise UserError('data transaksi tidak ditemukan')
        res['transaksi_ids'] = [(6, 0, transaksis.ids)]
        return res

    def action_simpan(self):
        transaksis = self.transaksi_ids
        buku_ids = transaksis.mapped('line_ids').mapped('buku_id')
        buku_ids.write({
            'available': True
        })
        transaksis.write({
            'state': 'selesai',
            'tanggal_kembali': self.tanggal_kembali
        })
        return True
