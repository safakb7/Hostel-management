from odoo import models,fields

class PosConfig(models.Model):
    _inherit = 'pos.config'

    is_discount_limit = fields.Boolean(string='Session Discount limit')
    discount_limit = fields.Float(string='Limit')
