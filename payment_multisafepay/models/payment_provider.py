import logging
import pprint

import requests

from odoo.addons.payment_multisafepay import const

from odoo import _, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import json

_logger = logging.getLogger(__name__)


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('multisafepay', 'Multisafepay')],
        ondelete={'multisafepay': 'set default'}
    )

    multisafepay_api_key = fields.Char(
        string="Multisafepay API Key",
        help="The Test or Live API Key depending on the configuration of the provider",
        required_if_provider="multisafepay"
    )

    def _get_supported_currencies(self):
        supported_currencies = super()._get_supported_currencies()
        if self.code == 'multisafepay':
            supported_currencies = supported_currencies.filtered(
                lambda c: c.name in const.SUPPORTED_CURRENCIES
            )
        return supported_currencies


    def _multisafepay_make_request(self, endpoint, data=None, method='POST'):
        self.ensure_one()

        url ='https://testapi.multisafepay.com/v1/json/orders?api_key=09984e450cb6315f7a2ba3106dc4d2a84cbd3c4c'

        headers = {
            'Content-Type': 'application/json',
            'accept': 'application/json',
        }
        try:
            if method == 'GET':
                print('ddd', data)
                url = 'https://testapi.multisafepay.com/v1/json/orders/S00060-6?api_key=09984e450cb6315f7a2ba3106dc4d2a84cbd3c4c'
                response = requests.get(url, headers=headers, timeout=10)
                print( response)
            else:
                response = requests.post(url, data=json.dumps(data), headers=headers, timeout=10)
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                _logger.exception(
                    "Invalid API request at %s with data:\n%s", url, pprint.pformat(data),
                )
                raise ValidationError("Flutterwave: " + _(
                    "The communication with the API failed. Flutterwave gave us the following "
                    "information: '%s'", response.json().get('message', '')
                ))
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            _logger.exception("Unable to reach endpoint at %s", url)
            raise ValidationError(
                "Flutterwave: " + _("Could not establish the connection to the API.")
            )
        return response
        # self.ensure_one()
        # endpoint = f'/v2/{endpoint.strip("/")}'
        # url ='https://testapi.multisafepay.com/v1/json/orders?api_key=09984e450cb6315f7a2ba3106dc4d2a84cbd3c4c'
        # print("endpoint",endpoint)
        # print("url",url)
        #
        # headers = {
        #     'Content-Type': 'application/json',
        #     'accept': 'application/json',
        # }
        # print("headers", headers)
        # print("data", data)
        # print(type(data))
        # try:
        #
        #     response = requests.request(method, url ,headers=headers ,data=json.dumps(data),
        #                                 timeout=60)
        #     print("response",response)
        #     try:
        #         response.raise_for_status()
        #     except requests.exceptions.HTTPError:
        #         _logger.exception(
        #             "Invalid API request at %s with data:\n%s", url,
        #             pprint.pformat(data)
        #         )
        #         raise ValidationError(
        #             "Multisafepay: " + _(
        #                 "The communication with the API failed. Multisafepay gave us the following "
        #                 "information: %s", response('detail', '')
        #             ))
        # except (
        # requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        #     _logger.exception("Unable to reach endpoint at %s", url)
        #     raise ValidationError(
        #         "Multisafepay: " + _("Could not establish the connection to the API.")
        #     )
        # return response

    def _get_default_payment_method_codes(self):
        default_codes = super()._get_default_payment_method_codes()
        if self.code != 'multisafepay':
            return default_codes
        return const.DEFAULT_PAYMENT_METHODS_CODES
