import os

from cvat.settings.production import *

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.environ["SMTP_HOST"]
EMAIL_PORT = int(os.getenv("SMTP_PORT", "587"))
EMAIL_HOST_USER = os.environ["SMTP_USERNAME"]
EMAIL_HOST_PASSWORD = os.environ["SMTP_PASSWORD"]

EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL = os.environ["SMTP_FROM"]
SERVER_EMAIL = DEFAULT_FROM_EMAIL

EMAIL_TIMEOUT = 20
