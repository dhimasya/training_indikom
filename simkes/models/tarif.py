from odoo import api, fields, models

class Tarif(models.Model):
    _name = 'tarif'
    _rec_name = 'nama'

    nama = fields.Char(required=True)
    kode = fields.Char(required=True)