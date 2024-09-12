from odoo import http
from odoo.http import request

class ConfirmQuotation(http.Controller):
    @http.route(['/my/quotation/confirm/<int:order_id>'], type='http',
                auth="public", website=True)

    def confirm_quotation(self,order_id):
        request.env['sale.order'].sudo().browse(order_id).action_confirm()
        return request.redirect('/my/orders')
