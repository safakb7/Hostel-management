from odoo import models
from odoo.exceptions import UserError
from datetime import date


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        discount_limit = float(self.env['ir.config_parameter'].sudo().get_param(
            'discount_limit.discount_limit'))
        print(discount_limit)
        monthly_record = self.env['sale.order'].search([
                ('date_order', 'like', date.today().strftime('%Y-%m'))
        ])
        print(monthly_record)
        total_discount = sum(monthly_record.order_line.mapped('discount_amount'))
        print(total_discount)
        if total_discount > discount_limit:
            raise UserError('The monthly discount limit has been exceeded.')
        else:
            return super().action_confirm()
