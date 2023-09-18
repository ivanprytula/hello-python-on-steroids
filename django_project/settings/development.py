from .base import *  # noqa
from .base import env

# -------------------------  GENERAL  ---------------------------------------
DEBUG = env.bool("DJANGO_DEBUG", default=True)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="my-secret-key",
)
ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]

# ------------------------  CACHES  --------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# ------------------------  EMAIL  ---------------------------------------
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)

# --------------------------- ADMIN -------------------------------------------
ADMIN_URL = "admin/"

# ---------------------------  WhiteNoise  --------------------------------------
# Django doesn't support serving static assets in a production-ready way, so we use the
# excellent WhiteNoise package to do so instead. The WhiteNoise middleware must be listed
# after Django's `SecurityMiddleware` so that security redirects are still performed.
# See: https://whitenoise.readthedocs.io
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")  # noqa: F405
INSTALLED_APPS += ["whitenoise.runserver_nostatic"]  # noqa: F405
WHITENOISE_INDEX_FILE = True

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# STATIC
# ------------------------

# django-debug-toolbar & django-browser-reload
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
INSTALLED_APPS += ["django_browser_reload"]  # noqa: F405
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],  # default
    "SHOW_TEMPLATE_CONTEXT": True,  # default
    "SHOW_COLLAPSED": True,  # default
}
INTERNAL_IPS = ["127.0.0.1"]


if env.bool("USE_DOCKER", default=False):
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]


# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["django_extensions"]  # noqa: F405

# django-silk
# ------------------------------------------------------------------------------
MIDDLEWARE += ["silk.middleware.SilkyMiddleware"]  # noqa: F405
INSTALLED_APPS += ["silk"]  # noqa: F405
SILKY_PYTHON_PROFILER = True

# django-webpack-loader
# ------------------------------------------------------------------------------
# WEBPACK_LOADER["DEFAULT"]["CACHE"] = not DEBUG  # noqa: F405

# ------------------------------- Celery ----------------------------------------
CELERY_TASK_EAGER_PROPAGATES = True

# --------------------------- SECURITY -------------------------------------------
# corresponding section for base.py + ...
# ----------------- SSL (secure sockets layer) -------------------
#  https://learndjango.com/tutorials/django-best-practices-security
# NB; get used to work in 'dev-prod parity' way
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 2592000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True


# python manage.py check --deploy
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
