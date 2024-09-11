# payment provider
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


# payment transaction
import logging
import pprint

from werkzeug import urls


from odoo.addons.payment_multisafepay.controllers.main import MultisafepayController

from odoo.addons.payment_multisafepay import const
from odoo import _, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'multisafepay':
            return res

        print("processing values", processing_values)
        payload = self._multisafepay_prepare_payment_request_payload()
        _logger.info("sending '/payments' request for link creation:\n%s",
                     pprint.pformat(payload))
        payment_data = self.provider_id._multisafepay_make_request('/payments',
                                                                   data=payload)
        print("provider",self.provider_id)

        response_data = payment_data.json()
        print("response_data", response_data)

        checkout_url = response_data['data']['payment_url']
        print("checkout", checkout_url)

        parsed_url = urls.url_parse(checkout_url)
        url_params = urls.url_decode(parsed_url.query)
        print(url_params)

        test = {'api_url': checkout_url, 'url_params': url_params}
        print("test", test)
        return test

    def _multisafepay_prepare_payment_request_payload(self):
        base_url = self.provider_id.get_base_url()
        return {
            'order_id': self.reference,
            'currency': self.currency_id.name,
            'amount': self.amount * 100,
            'description': self.reference,

            "payment_options": {
                "notification_url": urls.url_join(base_url,
                                                  MultisafepayController._notification_url),
                "notification_method": "POST",
                "redirect_url": urls.url_join(base_url,
                                              MultisafepayController._return_url),
            },
            "customer": {
                "first_name": self.partner_name,
                "last_name": self.partner_name,
                "address1": self.partner_address,
                "zip_code": self.partner_zip,
                "city": self.partner_city,
                "country": self.partner_country_id.name,
                "phone": self.partner_phone,
                "email": self.partner_email,
            }
        }

    def _get_tx_from_notification_data(self, provider_code, notification_data):
        tx = super()._get_tx_from_notification_data(provider_code,
                                                    notification_data)
        if provider_code != 'multisafepay' or len(tx) == 1:
            return tx

        print('notification_data', notification_data.get('transactionid'), notification_data)
        tx = self.search(
            [('reference', '=', notification_data.get('transactionid')),
             ('provider_code', '=', 'multisafepay')]
        )
        if not tx:
            raise ValidationError("Multisafepay: " + _(
                "No transaction found matching reference %s.",
                notification_data.get('ref')
            ))
        return tx

    def _process_notification_data(self, notification_data):
        super()._process_notification_data(notification_data)
        if self.provider_code != 'multisafepay':
            return

        payment_data = self.provider_id._multisafepay_make_request(
            f'/payments/{self.provider_reference}', method="GET" , data=notification_data
        )
        payment_data = payment_data.json()
        payment_method_type = payment_data.get('method', '')
        if payment_method_type == 'creditcard':
            payment_method_type = payment_data.get('details', {}).get(
                'cardLabel', '').lower()
        payment_method = self.env['payment.method']._get_from_code(
            payment_method_type, mapping=const.PAYMENT_METHODS_MAPPING
        )
        self.payment_method_id = payment_method or self.payment_method_id

        if payment_data.get('success'):
            payment_status = 'paid'

        if payment_status == 'pending':
            self._set_pending()
        elif payment_status == 'authorized':
            self._set_authorized()
        elif payment_status == 'paid':
            self._set_done()
        elif payment_status in ['expired', 'canceled', 'failed']:
            self._set_canceled(
                "Multisafepay: " + _("Canceled payment with status: %s",
                                     payment_status))
        else:
            _logger.info(
                "received data with invalid payment status (%s) for transaction with reference %s",
                payment_status, self.reference
            )
            self._set_error(
                "Multisafepay: " + _(
                    "Received data with invalid payment status: %s",
                    payment_status)
            )
