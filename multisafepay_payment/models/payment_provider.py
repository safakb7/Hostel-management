import logging


from odoo import _, fields, models


_logger = logging.getLogger(__name__)


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('multisafepay', 'Multisafepay')], ondelete={'multisafepay': 'set default'}
    )

    multisafepay_api_key = fields.Char(
        string="Multisafepay API Key",
        help="The Test or Live API Key depending on the configuration of the provider",
        required_if_provider="multisafepay"
    )