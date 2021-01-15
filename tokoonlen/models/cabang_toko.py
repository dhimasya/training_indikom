from odoo import models, fields


class CabangToko(models.Model):
    _name = 'cabang.toko'
    _description = 'tabel cabang toko'

    name = fields.Char()