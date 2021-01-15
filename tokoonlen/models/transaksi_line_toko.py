from odoo import models, fields


class TransaksiLineToko(models.Model):
    _name = 'transaksi.line.toko'
    _description = 'tabel transaksi line toko'

    name = fields.Char()
    cabang_id = fields.Many2one('cabang.toko')
    transaksi_id = fields.Many2one('transaksi.toko')
    produk_id = fields.Many2one('produk.toko')