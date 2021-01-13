# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class KategoriBuku(models.Model):
    _name = 'kategori.buku'
    _description = 'tabel kategori buku'

    name = fields.Char()

    def action_buka_list_buku(self):
        act = self.env.ref('perpus.buku_action2')
        action = act.read()[0]
        action['domain'] = [('kategori_id', 'in', self.ids)]
        return action
