from odoo.addons.payment import setup_provider, reset_payment_provider
from . import models

def post_init_hook(env):
    setup_provider(env, 'multisafepay')


def uninstall_hook(env):
    reset_payment_provider(env, 'multisafepay')
