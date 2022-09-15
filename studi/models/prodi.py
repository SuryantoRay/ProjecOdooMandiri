from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Prodi(models.Model):
    _name = 'studi.prodi'
    _description = 'New Description'

    name = fields.Selection([
        ('D3 Teknologi Informasi', 'D3 Teknologi Informasi'),
        ('D3 Teknologi Komputer', 'D3 Teknologi Komputer'),
        ('D4 Teknologi Rekayasa Perangkat Lunak', 'D4 Teknologi Rekayasa Perangkat LUnak'),
        ('S1 Informatika', 'S1 Informatika'),
        ('S1 Sistem Informasi', 'S1 Sistem Informasi'),
        ('S1 Teknik Elektro', 'S1 Teknik Elektro'),
        ('S1 Menajemen Rekayasa', 'S1 Menajemen Rekayasa'),
        ('S1 Bioproses', 'S1 Bioproses'),
    ], string='Program Studi', required=True)

    kode_prodi = fields.Char(string="Kode Program Studi")

    @api.onchange('name')
    def _onchange_kode_prodi(self):
        if self.name == 'D3 Teknologi Informasi':
            self.kode_prodi = 'D3 TI'
        elif self.name == 'D3 Teknologi Komputer':
            self.kode_prodi = 'D3 NM'
        elif self.name == 'D4 Teknologi Rekayasa Perangkat Lunak':
            self.kode_prodi = 'D4 TRPL'
        elif self.name == 'S1 Informatika':
            self.kode_prodi = 'S1 IF'
        elif self.name == 'S1 Sistem Informasi':
            self.kode_prodi = 'S1 SI'
        elif self.name == 'S1 Teknik Elektro':
            self.kode_prodi = 'S1 TE'
        elif self.name == 'S1 Menajemen Rekayasa':
            self.kode_prodi = 'S1 MR'
        elif self.name == 'S1 Bioproses':
            self.kode_prodi = 'S1 BP'
        elif self.name == '':
            raise ValidationError('Harus Memilih Program Studi')

    jumlah_kelas = fields.Char(compute='_compute_jumlah_kelas', string='Jumlah Kelas')

    kelas_id = fields.One2many(comodel_name='studi.kelas',
                               inverse_name='prodi_id',
                               string="Daftar Kelas")

    @api.depends('kelas_id')
    def _compute_jumlah_kelas(self):
        for record in self:
            a = self.env['studi.kelas'].search([('prodi_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.daftar = a

            if b == 0:
                record.jumlah_kelas = "Tidak Ada kelas"
            else:
                record.jumlah_kelas = b

    daftar = fields.Char(string="Daftar Isi")

    jumlah_mahasiswa = fields.Char(compute='_compute_jumlah_mahasiswa', string='Jumlah Mahasiswa')

    mahasiswa_id = fields.One2many(comodel_name='studi.mahasiswa',
                                       inverse_name='prodi_id',
                                       string='Daftar Mahasiswa')

    @api.depends('mahasiswa_id')
    def _compute_jumlah_mahasiswa(self):
        for record in self:
            a = self.env['studi.mahasiswa'].search([('prodi_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.daftar1 = a

            if b == 0:
                record.jumlah_mahasiswa = "Tidak ada Mahasiswa"
            else:
                record.jumlah_mahasiswa = b

    daftar1 = fields.Char(string="Daftar Isi")

    gambar = fields.Image(string='Gambar', required=True)