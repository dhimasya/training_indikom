from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    cabang_ids = fields.Many2many('cabang.toko')
