from odoo import api, fields, models

class Billing(models.Model):
    _name = 'billing'
    _rec_name = 'nama'

    nama = fields.Char(compute='_get_nama', store=True)
    kunjungan_id = fields.Many2one('kunjungan')
    kelas_id = fields.Many2one('kelas', required=True)
    tarif_id = fields.Many2one('tarif', required=True)
    catatan = fields.Char()
    jumlah = fields.Float()

    @api.depends('tarif_id', 'kelas_id')
    def _get_nama(self):
        for record in self:
            record.nama = "%s %s" % (record.kelas_id.display_name, record.tarif_id.display_name)

    @api.onchange('kelas_id')
    def onchange_kelas_id(self):
        tarif_kelas_ids = self.env['tarif.kelas'].search([
            ('kelas_id', '=', self.kelas_id.id)
        ])
        tarifs = tarif_kelas_ids.mapped('tarif_id')
        return {
            'domain': {
                'tarif_id': [('id', 'in', tarifs.ids)],
            }
        }

    @api.onchange('tarif_id')
    def onchange_tarif_id(self):
        jumlah = 0
        tarif_kelas = self.env['tarif.kelas'].search([
            ('kelas_id', '=', self.kelas_id.id),
            ('tarif_id', '=', self.tarif_id.id),
        ], limit=1)
        if tarif_kelas:
            jumlah = tarif_kelas.jumlah
        self.jumlah = jumlah