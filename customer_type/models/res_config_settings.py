from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    customer = fields.Char(string='customer type',config_parameter=
                                       'customer_type.customer')
