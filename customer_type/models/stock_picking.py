from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'


selected_customer = fields.Many2one('customer.type', 'customer',
                                    readonly=True)
