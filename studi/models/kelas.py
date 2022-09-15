from odoo import api, fields, models

class Kelas(models.Model):
    _name = 'studi.kelas'
    _description = 'New Description'

    name = fields.Char(string='Nama Kelas', required=True)
    angkatan = fields.Char(string="Angkatan", required=True)

    prodi_id = fields.Many2one(comodel_name='studi.prodi',
                               string="Program Studi",
                               ondelete='cascade')

    kapasitas = fields.Integer(string="Kapasitas Kelas", required=True)

    jumlah_mahasiswa = fields.Char(compute='_compute_jumlah_mahasiswa', string='Jumlah Mahasiswa')

    mahasiswa_id = fields.One2many(comodel_name='studi.mahasiswa',
                                   inverse_name='kelas_id',
                                   string='Daftar Mahasiswa')

    @api.depends('mahasiswa_id')
    def _compute_jumlah_mahasiswa(self):
        for record in self:
            a = self.env['studi.mahasiswa'].search([('kelas_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.daftar = a
            if b == 0:
                record.jumlah_mahasiswa = "Tidak Ada Mahasiswa"
            else:
                record.jumlah_mahasiswa = b

    @api.depends('mahasiswa_id')
    def _compute_kapasitas(self):
        for record in self:
            a = self.env['studi.mahasiswa'].search([('kelas_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.kurang = record.kapasitas - b


    daftar = fields.Char(string="Daftar Isi")
    kurang = fields.Integer(compute="_compute_kapasitas",string="Kuota Kosong")