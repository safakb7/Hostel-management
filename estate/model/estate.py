from datetime import timedelta

from odoo import models, fields

class Estate(models.Model):

    _name = "estate"

    name = fields.Char("Title")
    description = fields.Text("Description")
    postcode = fields.Char("postcode")
    expected_price = fields.Float("Expected price")
    bedrooms = fields.Integer("Bedrooms",default="2")
    facades = fields.Integer("Facades")
    garden = fields.Boolean("Garden")

    garden_orientation = fields.Selection(selection=[
        ('north', 'north'),
        ('south', 'south'),
        ('east', 'east'),
        ('west', 'west')
    ])
    available_from=fields.Date("Available from",default=fields.Date.today() + timedelta (days=92),copy=False)
    selling_price=fields.Float("Selling price",readonly=True,copy=False)
    living_area=fields.Integer("Living area(sqm)")
    garage=fields.Boolean("Garage")
    garden_area=fields.Integer("Garden area(sqm)")
    active=fields.Boolean("Active",default=True)
    state = fields.Selection(string="state",selection=[
        ('new', 'new'),
        ('offer recieved', 'offer recieved'),
        ('offer accepted', 'offer accepted'),
        ('sold', 'sold'),
        ('cancelled','cancelled')
    ],required=True,copy=False,default="new")




# .filtered(
#             lambda x: x.partner_id == self.partner_id and
#                       x.date_order.month == self.date_order.month
#
#          )


 # @api.onchange('product_id')
#
# def _onchange_product(self):
#     if self.order_id.partner_id.is_only_ordered and self.product_id:
#         if self.product_id.invoice_policy != 'order':
#             raise ValidationError("select only ordered qty product")
