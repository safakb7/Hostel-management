from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_discount_limit = fields.Boolean(string='Session Discount limit',
                                       config_parameter=
                                       'session_discount.is_discount_limit')
    discount_limit = fields.Float(string='Limit',
                                  config_parameter=
                                  'session_discount.discount_limit')
