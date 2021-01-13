# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class Anggota(models.Model):
    _name = 'anggota'
    _description = 'tabel anggota'
    _rec_name = 'nama'

    nama = fields.Char(required=True)
    tanggal_lahir = fields.Date(required=True)
    alamat = fields.Text(required=True)
    telfon = fields.Char(required=True)
    email = fields.Char()
    dibuat_dari = fields.Char()

    @api.model_create_multi
    def create(self, vals_list):
        from_transaksi = self._context.get('from_transaksi', False)
        if from_transaksi:
            new_vals_list = []
            for vals in vals_list:
                vals['dibuat_dari'] = 'transaksi'
                new_vals_list.append(vals)
            vals_list = new_vals_list
        return super(Anggota, self).create(vals_list)
