from odoo import api,fields,models
from odoo.exceptions import ValidationError


class Dosen(models.Model):
    _name = 'studi.dosen'
    _description = 'New Description'

    name = fields.Char(string="Nama")
    nis = fields.Char(string="NIS")
    tgl_lahir = fields.Date(string="Tanggal Lahir")
    inisial = fields.Char(string="Inisial")
    matakuliah_id = fields.One2many(comodel_name="studi.matakuliah",
                                    inverse_name="dosen_id",
                                    string="Matakuliah Diampu")

class Kprodi(models.Model):
    _name = 'studi.kprodi'
    _inherit = 'studi.dosen'
    _description = 'New Description'

    id_kprodi = fields.Char(string="ID Kepala Prodi")

    prodi_id = fields.Selection([
        ('D3 Teknologi Informasi', 'D3 Teknologi Informasi'),
        ('D3 Teknologi Komputer', 'D3 Teknologi Komputer'),
        ('D4 Teknologi Rekayasa Perangkat Lunak', 'D4 Teknologi Rekayasa Perangkat LUnak'),
        ('S1 Informatika', 'S1 Informatika'),
        ('S1 Sistem Informasi', 'S1 Sistem Informasi'),
        ('S1 Teknik Elektro', 'S1 Teknik Elektro'),
        ('S1 Menajemen Rekayasa', 'S1 Menajemen Rekayasa'),
        ('S1 Bioproses', 'S1 Bioproses'),
    ], string='Dosen Kepala Program Studi', required=True)

    @api.onchange('prodi_id')
    def _onchange_kode_prodi(self):
        if self.prodi_id == 'D3 Teknologi Informasi':
            self.id_kprodi = '130KP0TI'
        elif self.prodi_id == 'D3 Teknologi Komputer':
            self.id_kprodi = '130KP0NM'
        elif self.prodi_id == 'D4 Teknologi Rekayasa Perangkat Lunak':
            self.id_kprodi = '140KP0TRPL'
        elif self.prodi_id == 'S1 Informatika':
            self.id_kprodi = '120KP0IF'
        elif self.prodi_id == 'S1 Sistem Informasi':
            self.id_kprodi = '12S0KP0SI'
        elif self.prodi_id == 'S1 Teknik Elektro':
            self.id_kprodi = '12E0KP0TE'
        elif self.prodi_id == 'S1 Menajemen Rekayasa':
            self.id_kprodi = '150KP0MR'
        elif self.prodi_id == 'S1 Bioproses':
            self.id_kprodi = '1340KP0BP'
        elif self.prodi_id == '':
            raise ValidationError('Harus Memilih Program Studi')

    _sql_constraints = [
        ('id_kprodi_unik', 'unique (id_kprodi)', 'Kepala Program Sudah ada')
    ]

