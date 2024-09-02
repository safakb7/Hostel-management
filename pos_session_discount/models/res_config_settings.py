from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_discount_limit = fields.Boolean(related='pos_config_id.is_discount_limit',
                                       readonly=False)
    discount_limit = fields.Float(related='pos_config_id.discount_limit',
                                  readonly=False)
