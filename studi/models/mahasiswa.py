from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Mahasiswa(models.Model):
    _name = 'studi.mahasiswa'
    _description = 'New Description'

    name = fields.Char(string="Nama", required=True)
    tmp_lahir = fields.Char(string='Tempat Lahir', required=True)
    tgl_lahir = fields.Date(string="Tanggal Lahir", required=True)
    umur = fields.Char(string='Umur', required=True)
    alamat = fields.Char(string='Alamat', required=True)
    semester = fields.Char(string="Semester", required=True, default="1")
    pdd_terakhir = fields.Char(string='Pendidikan Terakhir', required=True)
    jumlah_sks = fields.Char(compute="_compute_matakuliah" ,string="Jumlah SKS yang di Ambil")

    prodi_id = fields.Many2one(comodel_name='studi.prodi',
                               string='Program Studi',
                               ondelete='cascade')

    matakuliah_id = fields.Many2many(comodel_name='studi.matakuliah',
                                     string="Matakuliah")

    # @api.model
    # def create(self, vals):
    #     line = super(Mahasiswa, self).create(vals)
    #     self.env['studi.kelas'].search(
    #         [('id', '=', line.kelas_id.id)]
    #     ).write({'kapasitas': line.kelas_id.kapasitas - 1})
    #
    #     return line

    @api.depends('matakuliah_id')
    def _compute_matakuliah(self):
        for line in self:
            result = sum(self.env['studi.matakuliah'].search(
                [('mahasiswa_id', '=', line.id)]).mapped('sks'))
            line.jumlah_sks = result

    @api.constrains('matakuliah_id')
    def chek_matakuliah(self):
        erorr = []
        for list in self:
            chek = self.env['studi.matakuliah'].search(
                [('mahasiswa_id', '=', list.id)]
            ).mapped('semester')

            erorr = chek
        jm = 0
        for ab in erorr:
            if ab != self.semester:
                jm += 1

        if jm != 0:
            raise ValidationError(f"Terdapat {jm} Matakuliah yang tidak sesuai dengan semester anda")

    @api.constrains('prodi_id', 'kelas_id')
    def check_data(self):
        if self.prodi_id.id != self.kelas_id.prodi_id.id:
            raise ValidationError('Kelas Tidak Sesuai dengan program studi')

    # @api.constrains('matakuliah_id')
    # def check_matkul(self):
    #     print(self.matakuliah_id.name)
    #     for line in self:
    #         print(line.matakuliah_id.semester)
    #         if line.matakuliah_id.semester != line.semester:
    #             raise ValidationError('Anda belum bisa ambil matakuliah ini')

    # @api.depends('prodi_id')
    # def _compute_kelas(self):
    #     for record in self:
    #         a = self.env['studi.kelas'].search([('prodi_id', '=', record.prodi_id.id)]).mapped('name')
    #         print(a)
    #         record.kelas_id = a

    kelas_id = fields.Many2one(comodel_name='studi.kelas', string='Kelas')