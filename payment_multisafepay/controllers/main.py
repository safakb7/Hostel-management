import pprint

from odoo import http
from odoo.http import request


class MultisafepayController(http.Controller):
    _return_url = '/payment/multisafepay/return'
    _webhook_url = '/payment/multisafepay/webhook'

    @http.route(
        _return_url, type='http', auth='public', methods=['GET', 'POST'],
        csrf=False,
        save_session=False )

    def multisafepay_return_from_checkout(self, _logger=None, **data):

        _logger.info("handling redirection from Mollie with data:\n%s",
                     pprint.pformat(data))
        request.env['payment.transaction'].sudo()._handle_notification_data(
            'mollie', data)
        return request.redirect('/payment/status')

