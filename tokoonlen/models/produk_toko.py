from odoo import models, fields


class ProdukToko(models.Model):
    _name = 'produk.toko'
    _description = 'tabel produk toko'

    name = fields.Char()