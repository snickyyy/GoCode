from config.settings.base import *  # NOQA

SECRET_KEY = "django-insecure-6qxpqn(kzeka89cf=ucx&nctbet_2z#%+grri8(8l5_xqw0n9v"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS += []  # NOQA

INSTALLED_APPS += []  # NOQA

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}

STATIC_URL = "static/"
