from .base import *  # noqa
from .base import env

# -------------------------  GENERAL  ---------------------------------------
DEBUG = True
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

# ---------------------------  WhiteNoise  --------------------------------------
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa: F405

# django-debug-toolbar & django-browser-reload
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["debug_toolbar", "django_browser_reload"]  # noqa: F405
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

# django-webpack-loader
# ------------------------------------------------------------------------------
WEBPACK_LOADER["DEFAULT"]["CACHE"] = not DEBUG  # noqa: F405

# ------------------------------- Celery ----------------------------------------
CELERY_TASK_EAGER_PROPAGATES = True
