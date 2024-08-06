from odoo import models,fields


class Patient(models.Model):

    _inherit = "res.partner"

    age = fields.Integer(string="Age")
    blood_group = fields.Selection(selection=[
        ('A+','A+'),
        ('B+','B+'),
    ])
    gender = fields.Selection(selection=[
        ('female', 'female'),
        ('male', 'male'),
    ])
    date_of_birth = fields.Date(string="DOB")
    sequence = fields.Char(string="sequence")

