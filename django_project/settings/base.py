"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

import environ

env = environ.Env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Take environment variables from .env file
# OS environment variables take precedence over variables from .env
env.read_env(str(BASE_DIR / ".env"))
APPS_DIR = BASE_DIR / "apps"

# -------------------------  GENERAL  ---------------------------------------
DEBUG = env.bool("DJANGO_DEBUG", default=False)

LANGUAGE_CODE = "en-us"

SITE_ID = 1
SITE_NAME = "Hello Python on steroids"

TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# -------------------------  DATABASES  -----------------------------------
# >>> # This will run on the 'default' database.
# >>> Author.objects.all()

# >>> # So will this.
# >>> Author.objects.using("default")

# >>> # This will run on the 'sandbox_db' database.
# >>> Author.objects.using("sandbox_db")

DATABASES = {
    "default": env.db(
        var="DATABASE_URL", default=f"sqlite:///{BASE_DIR}/db.sqlite3", engine="django.db.backends.sqlite3"
    ),
    "sandbox_db": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

DATABASES["default"]["ATOMIC_REQUESTS"] = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ----------------------------  URLS  ------------------------------------
ROOT_URLCONF = "django_project.urls"
WSGI_APPLICATION = "django_project.wsgi.application"

# ---------------------------  APPS  ------------------------------------------

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # ... include the providers you want to enable:
    # https://django-allauth.readthedocs.io/en/latest/installation.html
    "django_celery_beat",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "drf_spectacular",
    "django_filters",
    "webpack_loader",
]
LOCAL_APPS = [
    "apps.common",
    "apps.users",
    "apps.pages",
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ------------------------  AUTHENTICATION  ---------------------------------
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "users:redirect"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
LOGIN_URL = "account_login"

# ------------------------  PASSWORDS  --------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------  MIDDLEWARE  ---------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ------------------------  STATIC  ------------------------------------------
# 1. set STATIC_ROOT
# 2. collectstatic --noinput: copy from all STATICFILES_DIRS and put into "staticfiles"
# 3. Use a web server of your choice to serve the files

# STATIC_URL is the URL location of static files located in STATIC_ROOT
# STATICFILES_DIRS tells Django where to look for static files in a Django project, such as a top-level static folder
# STATIC_ROOT is the folder location of static files when collectstatic is run
# STATICFILES_STORAGE is the file storage engine used when collecting static files with the collectstatic command.

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"  # Url from which static files are served
STATICFILES_DIRS = [str(APPS_DIR / "static")]

# ------------------------  MEDIA  -----------------------------------------------
MEDIA_ROOT = str(APPS_DIR / "media")
MEDIA_URL = "/media/"

# ---------------------  TEMPLATES  --------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                # `allauth` needs this from django
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "users.context_processors.allauth_settings",
                "apps.common.context_processors.site_name",
            ],
        },
    },
]

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# ------------------  django-crispy-forms  ---------------------------------------
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# --------------------------- SECURITY -------------------------------------------
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# --------------------------- EMAIL -------------------------------------------
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
EMAIL_TIMEOUT = 5

# --------------------------- ADMIN -------------------------------------------
ADMIN_URL = "admin/"
ADMINS = [("""Ivan Prytula""", "ivan-prytula@example.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# https://cookiecutter-django.readthedocs.io/en/latest/settings.html#other-environment-settings
# Force the `admin` sign in process to go through the `django-allauth` workflow
DJANGO_ADMIN_FORCE_ALLAUTH = env.bool("DJANGO_ADMIN_FORCE_ALLAUTH", default=False)


# -------------------------  LOGGING  -----------------------------------------
LOGGING = {
    # Define the logging version
    "version": 1,
    # Enable the existing loggers
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s - %(asctime)s - %(message)s",
            # "format": "%(name)s ~ %(levelname)s %(levelno)s - %(asctime)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "[ {levelname} ] {lineno} {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "filters": ["require_debug_true"],
            "formatter": "verbose",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "./logs/verbose_debug.log",
            "formatter": "simple",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["file"],
            "level": "ERROR",
            #  log messages written to django.request will not be handled by the 'django' logger
            "propagate": False,
        },
    },
}

# -----------------------  django-allauth  -----------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_ADAPTER = "users.adapters.AccountAdapter"
ACCOUNT_FORMS = {"signup": "users.forms.UserSignupForm"}
SOCIALACCOUNT_FORMS = {"signup": "users.forms.UserSocialSignupForm"}
ACCOUNT_UNIQUE_EMAIL = True

# -------------------  django-rest-framework  ---------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    # "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
}

CORS_URLS_REGEX = r"^/api/.*$"

# By Default swagger ui is available only to admin user(s). You can change permission classes to change that
SPECTACULAR_SETTINGS = {
    "TITLE": "price-navigator API",
    "DESCRIPTION": "Documentation of API endpoints of price-navigator",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
}

# django-webpack-loader
# ------------------------------------------------------------------------------
WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "STATS_FILE": BASE_DIR / "webpack-stats.json",
        "POLL_INTERVAL": 0.1,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    }
}

# Your stuff...
# ------------------------------------------------------------------------------
