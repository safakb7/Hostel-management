from odoo import models, fields


class StudentRegister(models.Model):
    _name = 'student.register'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')

