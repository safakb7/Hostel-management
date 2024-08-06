from odoo import models, fields


class Specialization(models.Model):

    _name = "specialization"
    name = fields.Char(string="Name")

