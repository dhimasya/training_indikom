from odoo import api, fields, models

class Kunjungan(models.Model):
    _name = 'kunjungan'
    _rec_name = 'nomor'

    nomor = fields.Char()
    kelas_id = fields.Many2one('kelas', required=True)
    billing_ids = fields.One2many('billing', 'kunjungan_id')


    @api.onchange('kelas_id')
    def onchange_kelas_id(self):
        self.billing_ids = False
