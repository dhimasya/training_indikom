# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class Buku(models.Model):
    _inherit = 'buku'

    review = fields.Html()