from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w-z$x0b8n1kwf+00-o+5)*j-zf8alwpp_nj@i^s5wsse+nb!a1'

DEBUG = env.bool('DJANGO_DEBUG', default=True)
