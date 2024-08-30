from odoo import models, fields


class CustomerType(models.Model):
    _name = 'customer.type'
    _description = 'customer'

    customer_type = fields.Char('Customer Type')

    user_id = fields.Many2one('res.users')

    def button_validate(self):
        customer_field = self.env['ir.config_parameter'].sudo().get_param(
            'customer_type.customer')

        if customer_field == self.customer_type:
            return super().button_validate()
