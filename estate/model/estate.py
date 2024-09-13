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



# odoo.define('your_module_name.quantity_adjustment', function (require) {
#     'use strict';
#
#     var publicWidget = require('web.public.widget');
#     var WebsiteSale = require('website_sale.website_sale');
#
#     // Override the WebsiteSale widget
#     publicWidget.registry.WebsiteSale.include({
#
#         // Override the _onClickAdd function to add 0.1 to the quantity
#         _onClickAdd: function (ev) {
#             ev.preventDefault();
#             var $input = $(ev.currentTarget).closest('.input-group').find('input');
#             var oldValue = parseFloat($input.val()) || 0;
#             var newValue = oldValue + 0.1;
#             $input.val(newValue.toFixed(1)).trigger('change');
#         },
#
#         // Override the _onClickRemove function to subtract 0.1 from the quantity
#         _onClickRemove: function (ev) {
#             ev.preventDefault();
#             var $input = $(ev.currentTarget).closest('.input-group').find('input');
#             var oldValue = parseFloat($input.val()) || 0;
#             var newValue = oldValue - 0.1;
#             if (newValue >= 0) {  // Ensure the quantity doesn't go below 0
#                 $input.val(newValue.toFixed(1)).trigger('change');
#             }
#         }
#     });
# });
#
#
#
#
#
# odoo.define('your_module_name.website_sale', function (require) {
#     'use strict';
#
#     var publicWidget = require('web.public.widget');
#     publicWidget.registry.WebsiteSale.include({
#         /**
#          * Override the _onClickAdd and _onClickRemove methods to increment/decrement by 0.1
#          */
#         _onClickAdd: function (ev) {
#             var $input = $(ev.currentTarget).closest('.input-group').find('input');
#             var value = parseFloat($input.val()) || 0;
#             $input.val((value + 0.1).toFixed(1)).trigger('change');
#         },
#         _onClickRemove: function (ev) {
#             var $input = $(ev.currentTarget).closest('.input-group').find('input');
#             var value = parseFloat($input.val()) || 0;
#             if (value > 0.1) {
#                 $input.val((value - 0.1).toFixed(1)).trigger('change');
#             }
#         },
#     });
# });
#
