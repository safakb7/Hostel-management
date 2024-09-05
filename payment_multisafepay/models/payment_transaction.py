import logging
import pprint

from werkzeug import urls

from addons2.payment_multisafepay.controllers.main import MultisafepayController
from odoo import _, models


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
        payment_data = self.provider_id._mollie_make_request('/payments',
                                                             data=payload)

        self.provider_reference = payment_data.get('id')

    def _multisafepay_prepare_payment_request_payload(self):

        user_lang = self.env.context.get('lang')
        base_url = self.provider_id.get_base_url()
        redirect_url = urls.url_join(base_url, MultisafepayController._return_url)
        webhook_url = urls.url_join(base_url, MultisafepayController._webhook_url)


        return{
            "type": self.type,
            "order_id": self.order_id,
            "currency": self.currency,
            "amount": self.amount,
        "description": self.description,
        }
