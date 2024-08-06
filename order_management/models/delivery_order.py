from odoo import models, fields, api


class DeliveryOrder(models.Model):
    _inherit = 'stock.picking'

    salesperson = fields.Many2one('res.users',string="salesperson")

    def button_validate(self):
        self.salesperson = self.sale_id.user_id.id
        print(self.salesperson)



