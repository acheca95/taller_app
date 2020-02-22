from odoo import fields,models

class Taller(models.Model):
	_name = "taller.datos"
	#nama
	Nombre = fields.Char(size=32,string="Nombre")
	#kelas
	Localizacion = fields.Char(size=32,string="Localizacion")
	#alamat
	Web = fields.Char(size=32,string="Web")
	Abierto = fields.Boolean('Abierto',default=False)
