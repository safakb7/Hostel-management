from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    client_order_ref = fields.Char('Client Reference')

    @api.constrains('client_order_ref')
    def client_order_ref(self):
        for order in self:
            if order.client_order_ref:
                client =  self.search([('client_order_ref', '=', order.client_order_ref),
                                       ('id', '!=', order.id)], limit=1)
                return client
