from odoo import models


class PosSession(models.Model):
    _inherit = 'pos.session'

    def get_discount(self):
        return sum(self.order_ids.lines.mapped('discount_amount'))
