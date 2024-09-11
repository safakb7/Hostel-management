from odoo import http
from odoo.http import request


class ConfirmQuotation(http.Controller):
    @http.route(['/my/orders'], type='json', auth="public",
                website=True)
    def confirm_quotation(self):
        print("edhuiv")
        order = request.website.sale_get_order()
        print(order)
