from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    range_slider = fields.Integer(string="Range Slider")
