import pprint

from werkzeug.exceptions import Forbidden

from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request, _logger


class MultisafepayController(http.Controller):
    _return_url = '/payment/multisafepay/return'
    _webhook_url = '/payment/multisafepay/webhook'

    @http.route(
        _return_url, type='http', auth='public', methods=['GET', 'POST'],
        csrf=False,
        save_session=False)
    def multisafepay_return_from_checkout(self, _logger=None, **data):

        _logger.info("handling redirection from Multisafepay with data:\n%s",
                     pprint.pformat(data))
        request.env['payment.transaction'].sudo()._handle_notification_data(
            'multisafepay', data)
        return request.redirect('/payment/status')

    @http.route(_webhook_url, type='http', auth='public', methods=['POST'],
                csrf=False)
    def multisafepay_webhook(self, **data):

        _logger.info("notification received from Multisafepay with data:\n%s",
                     pprint.pformat(data))
        try:
            request.env['payment.transaction'].sudo()._handle_notification_data(
                'multisafepay', data)
        except ValidationError:
            _logger.exception(
                "unable to handle the notification data; skipping to acknowledge")
        return ''

