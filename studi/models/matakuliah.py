from odoo import api, fields, models

class Matakuliah(models.Model):
    _name = 'studi.matakuliah'
    _description = 'New Description'

    name = fields.Char(string="Matakuliah", required=True)
    kode_mtk = fields.Char(string="Kode Matakuliah")
    sks = fields.Integer(string="SKS")
    semester = fields.Char(string="Semester", default="1")
    dosen_id = fields.Many2one(comodel_name="studi.dosen",
                               string="Dosen Pengampu")

    mahasiswa_id = fields.Many2many(comodel_name="studi.mahasiswa",
                                    string="Mahasiswa")

    @api.onchange('name')
    def _onchange_kode_mtk(self):
        self.kode_mtk = "MTK"

    _sql_constraints = [
        ('kode_mtk_unik', 'unique (kode_mtk)', 'Kode Matakuliah Sudah di Gunakan! tidak boleh sama!')
    ]