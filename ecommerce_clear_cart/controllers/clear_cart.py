from odoo import http
from odoo.http import request


class ClearCart(http.Controller):
    @http.route(['/shop/clear_cart'], type='json', auth="public",
                website=True)
    def clear_cart(self):
        """clear all shopping cart products """
        order = request.website.sale_get_order()
        order.website_order_line.unlink()

