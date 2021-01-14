from odoo import api, fields, models

class TarifKelas(models.Model):
    _name = 'tarif.kelas'
    _rec_name = 'kode'

    kode = fields.Char(compute='_get_kode', store=True)
    tarif_id = fields.Many2one('tarif', required=True)
    kelas_id = fields.Many2one('kelas', required=True)
    jumlah = fields.Float()

    @api.depends('tarif_id', 'kelas_id')
    def _get_kode(self):
        for record in self:
            record.kode = "%s %s" % (record.kelas_id.display_name, record.tarif_id.display_name)

    # @api.model_create_multi
    # def create(self, vals_list):
    #     vals_list[]
    #     res = super(TarifKelas, self).create(vals_list)
    #     for record in res:
    #         record.tarif_id.kelas_ids = [(0, 0, {
    #             'tarif_id': record.tarif_id.id,
    #             'kelas_id': record.kelas_id.id
    #         })]
    #     return res
