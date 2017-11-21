from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w-z$x0b8n1kwf+00-o+5)*j-zf8alwpp_nj@i^s5wsse+nb!a1'

DEBUG = env.bool('DJANGO_DEBUG', default=True)

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}