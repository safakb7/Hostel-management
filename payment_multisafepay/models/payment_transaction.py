import logging
import pprint

from werkzeug import urls

from odoo.addons.payment_multisafepay.controllers.main import \
    MultisafepayController
from odoo import _, models

_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'multisafepay':
            return res

        print(processing_values)

        payload = self._multisafepay_prepare_payment_request_payload()
        _logger.info("sending '/payments' request for link creation:\n%s",
                     pprint.pformat(payload))
        payment_data = self.provider_id._multisafepay_make_request('/payments',
                                                             data=payload)

        self.provider_reference = payment_data.get('id')

        checkout_url = payment_data['_links']['checkout']['href']
        parsed_url = urls.url_parse(checkout_url)
        url_params = urls.url_decode(parsed_url.query)
        return {'api_url': checkout_url, 'url_params': url_params}


    def _multisafepay_prepare_payment_request_payload(self, payment_utils=None):
        base_url = self.provider_id.get_base_url()
        # cancel_url = urls.url_join(base_url, MultisafepayController._cancel_url)
        # cancel_url_params = {
        #     'tx_ref': self.reference,
        #     'return_access_tkn': payment_utils.generate_access_token(
        #         self.reference),
        # }
        redirect_url = urls.url_join(base_url,
                                     MultisafepayController._return_url)
        webhook_url = urls.url_join(base_url,
                                    MultisafepayController._webhook_url)
        # partner_first_name, partner_last_name = payment_utils.split_partner_name(self.partner_name)


        return {
            'order_id': self.reference,
            'currency': self.currency_id.name,
            'amount': self.amount,
            'currency_code': self.currency_id.name,
            # 'first_name': partner_first_name,
            # 'last_name': partner_last_name,
            'address1': self.partner_address,
            'zip_code': self.partner_zip,
            'city': self.partner_city,
            'country': self.partner_country_id.code,
            'email': self.partner_email,

            # 'cancel_return': f'{cancel_url}?{urls.url_encode(cancel_url_params)}',

            'redirectUrl': f'{redirect_url}?ref={self.reference}',
            'webhookUrl': f'{webhook_url}?ref={self.reference}',
        }
