import logging
import pprint
from werkzeug import urls
from odoo.addons.payment_multisafepay.controllers.main import \
    MultisafepayController
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

        payload = self._multisafepay_prepare_payment_request_payload()
        _logger.info("sending '/payments' request for link creation:\n%s",
                     pprint.pformat(payload))
        payment_data = self.provider_id._multisafepay_make_request('',
                                                                   data=payload)
        response_data = payment_data.json()
        checkout_url = response_data['data']['payment_url']
        parsed_url = urls.url_parse(checkout_url)
        url_params = urls.url_decode(parsed_url.query)
        test = {'api_url': checkout_url, 'url_params': url_params}
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
            str(self.reference), method="GET", data=notification_data
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
        self.provider_reference = notification_data.get('transactionid')

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
