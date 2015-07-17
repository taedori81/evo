from .base import *


DEBUG = False
TEMPLATE_DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql.psycopg2',
#         'NAME': 'evo',
#         'USER': os.environ['DATABASE_USERNAME'],
#         'PASSWORD': os.environ['DATABASE_PASSWORD'],
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }


ALLOWED_HOSTS = ['byevo.com']

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = env('EMAIL_ADDRESS')
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

try:
    from .local import *
except ImportError:
    pass
