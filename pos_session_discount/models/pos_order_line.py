from odoo import models, fields, api


class PosConfig(models.Model):
    _inherit = 'pos.order.line'

    discount_amount = fields.Integer('Discount Amount',
                                  compute='_compute_discount_amount')


    @api.depends('price_unit','qty','price_subtotal_incl')
    def _compute_discount_amount(self):
        for rec in self:
            rec.discount_amount = (rec.qty *
                                    rec.price_unit-rec.price_subtotal)
