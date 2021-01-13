from odoo import models, fields, api

class Transaksi(models.Model):
    _name = 'transaksi'
    _description = 'tabel transaksi'
    _rec_name = 'nomor'

    nomor = fields.Char('Nomor')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('proses', 'Buku Keluar'),
        ('selesai', 'Buku Kembali'),
    ], default='draft')
    anggota_id = fields.Many2one('anggota', required=True)
    buku_id = fields.Many2one('buku')
    kategori_id = fields.Many2one('kategori.buku')
    line_ids = fields.One2many('transaksi.line', 'transaksi_id')
    tanggal_kembali = fields.Date()

    @api.onchange('kategori_id',)
    def onchange_kategori_id(self):
        line_ids = [(5, 0, 0)]
        if self.kategori_id:
            bukus = self.env['buku'].search([
                ('kategori_id', '=', self.kategori_id.id)
            ])
            for buku in bukus:
                line_ids.append([0, 0, {
                    'buku_id': buku.id,
                    'deskripsi': buku.deskripsi,
                }])
        self.write({
            'line_ids': line_ids
        })


    def action_konfirmasi(self):
        tipe = self._context.get('tipe', False)
        if tipe:
            if tipe == 'level1':
                buku_ids = self.line_ids.mapped('buku_id')
                buku_ids.available = False
            elif tipe == 'level2':
                self.state = 'proses'

    def action_kembali(self):
        res = self.env.ref('perpus.buku_kembali_action')
        return res.read()[0]


class TransaksiLine(models.Model):
    _name = 'transaksi.line'
    _rec_name = 'deskripsi'

    transaksi_id = fields.Many2one('transaksi')
    buku_id = fields.Many2one('buku')
    deskripsi = fields.Text()

    