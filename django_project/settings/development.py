# flake8: noqa

# from .base import *

# ALLOWED_HOSTS = ["*"]

# INSTALLED_APPS += ["debug_toolbar", "django_extensions", "silk"]

# DEBUG_TOOLBAR_CONFIG = {
#     "SHOW_COLLAPSED": True,
# }

# MIDDLEWARE += [
#     "debug_toolbar.middleware.DebugToolbarMiddleware",
#     "silk.middleware.SilkyMiddleware",
# ]

# INTERNAL_IPS = ["127.0.0.1"]

# ADMIN_EMAIL = "user@email.com"

# NOTEBOOK_ARGUMENTS = [
#     "--ip",
#     "0.0.0.0",
#     "--allow-root",
#     "--no-browser",
# ]

# # PRIVATE_MEDIA_STORAGE = "backend.storage_backends"
# DEFAULT_FILE_STORAGE = "backend.storage_backends.PrivateVolumeMediaStorage"


from .base import *  # noqa
from .base import env

# -------------------------  GENERAL  ---------------------------------------
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="my-secret-key",
)
ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]

# ------------------------  CACHES  --------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# ------------------------  EMAIL  ---------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)

# ---------------------------  WhiteNoise  --------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa: F405

# django-debug-toolbar & django-browser-reload
# ------------------------------------------------------------------------------
if env.bool("USE_DEBUG_TOOLBAR", default=DEBUG):
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
    INSTALLED_APPS += ["debug_toolbar", "django_browser_reload"]  # noqa: F405
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405
    # https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
    DEBUG_TOOLBAR_CONFIG = {
        "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
        # "SHOW_TEMPLATE_CONTEXT": True,
    }
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
    INTERNAL_IPS = ["127.0.0.1"]


if env.bool("USE_DOCKER", default=False):
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]


# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa: F405

# ------------------------------- Celery ----------------------------------------
