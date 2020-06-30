from typing import List
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Security
ALLOWED_HOSTS.append('localhost')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'  # TODO: hmmm
