from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-jcnk0@^3^$a*g02e76nwipxewgdyda5)j&0)8+uw6&#v--259w"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
