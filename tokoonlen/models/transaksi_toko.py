from odoo import models, fields, api


class TransaksiToko(models.Model):
    _name = 'transaksi.toko'
    _description = 'tabel transaksi toko'

    def _get_domain_cabang_id(self):
        user = self.env.user
        cabang_ids = []
        if user.cabang_ids:
            cabang_ids = user.cabang_ids.ids
        return [('id', 'in', cabang_ids)]

    def _get_default_cabang_id(self):
        user = self.env.user
        cabang_id = False
        if user.cabang_ids:
            cabang_id = user.cabang_ids.ids[0]
        return cabang_id

    name = fields.Char()
    kasir_id = fields.Many2one('res.users', default=lambda self: self.env.user, required=True)
    cabang_id = fields.Many2one('cabang.toko', domain=_get_domain_cabang_id, default=_get_default_cabang_id, required=True)
    line_ids = fields.One2many('transaksi.line.toko', 'transaksi_id')

    def action_cancel(self):
        return True

    @api.onchange('name')
    def onchange_name(self):
        print('hiiiiii')

    @api.model_create_multi
    def create(self, vals_list):
        print('sebelum create')
        return super(TransaksiToko, self).create(vals_list)

    