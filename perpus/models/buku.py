# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError, UserError

class Buku(models.Model):
    _name = 'buku'
    _description = 'tabel buku'

    name = fields.Char('Judul')
    deskripsi = fields.Text()
    tanggal_terbit = fields.Date(default=datetime.now())
    usia_buku = fields.Integer(compute='_compute_usia_buku')
    halaman = fields.Integer()
    available = fields.Boolean(default=True)
    color = fields.Integer()
    kategori_id = fields.Many2one('kategori.buku')

    # hindari non stored compute pada master data
    # lebih baik menggunakan scheduler untuk mendapatkan value
    # yang dapat di execute setiap dini hari
    # selain faktor performance, ada juga faktor penggunaan di advance view
    # seperti pivot dan graph
    @api.depends('tanggal_terbit')
    def _compute_usia_buku(self):
        for record in self:
            usia_buku = 0
            if record.tanggal_terbit:
                selisih = datetime.now().date() - record.tanggal_terbit
                usia_buku = selisih.days
            record.usia_buku = usia_buku

    # gunakan python constraint untuk pembatasan yang dimanis
    # untuk lebih detail tentang penggunaan constraint
    # https://www.odoo.com/documentation/14.0/howtos/backend.html?highlight=views#model-constraints
    @api.constrains('halaman')
    def _check_halaman_buku(self):
        for record in self:
            if record.halaman < 10:
                raise ValidationError("buku harus memiliki minimal 10 halaman")

    @api.model_create_multi
    def create(self, vals_list):
        # proses sebelum create
        for vals in vals_list:
            if len(vals.get('deskripsi', '')) < 10:
                raise UserError('minimal panjang deskripsi harus 10 karakter')
        res = super(Buku, self).create(vals_list)
        # proses setelah create
        return res

    def write(self, vals):
        # proses sebelum update
        res = super(Buku, self).write(vals)
        # proses setelah update
        return res

    def unlink(self):
        # proses sebelum hapus
        res = super(Buku, self).unlink()
        # proses setelah hapus
        return res

    def _format_tanggal_terbit(self):
        return self.tanggal_terbit.strftime('%d/%m/%Y')


    def action_print_buku(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': '/report/html/%s/%s' % ('perpus.buku_report_template', self.id),
        }
