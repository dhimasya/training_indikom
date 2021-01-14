from odoo import api, fields, models

class Kelas(models.Model):
    _name = 'kelas'
    _rec_name = 'nama'

    nama = fields.Char(required=True)
    kode = fields.Char(required=True)