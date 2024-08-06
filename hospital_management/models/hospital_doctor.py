from odoo import models,fields


class Doctor(models.Model):

    _inherit = "hr.employee"
    tags = fields.Many2many('specialization',string="Specialization")