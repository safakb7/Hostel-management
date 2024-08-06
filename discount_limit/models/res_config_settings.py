from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_discount_limit = fields.Boolean(string='Discount limit',
                                       config_parameter=
                                       'discount_limit.is_discount_limit')
    discount_limit = fields.Float(string='Limit amount',
                                  config_parameter=
                                  'discount_limit.discount_limit')
