from odoo import models, fields, api

class TransaksiReport(models.Model):
    _name = 'transaksi.report'
    _description = 'tabel transaksi report'
    _auto = False

    id = fields.Integer()
    name = fields.Char()
    cabang = fields.Char()

    @property
    def _table_query(self):
        return "select tt.id,tt.name,ct.name as cabang from transaksi_toko tt left join cabang_toko ct on tt.cabang_id = ct.id "

    def action_test(self):
        row = self.env['transaksi.toko'].sudo().browse(self.id)
        print(row.cabang_id.name)
        return True