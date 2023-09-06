"""
    Everything that we can set only once in the base.py and change its value using django-environ
    we should keep in the base.py and never repeat/override in the other settings modules.
 """

"""
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
# https://github.com/jazzband/django-redis#memcached-exceptions-behavior

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff


# https://docs.djangoproject.com/en/dev/topics/i18n/
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
# https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-USE_I18N
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz

# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# NB: https://docs.djangoproject.com/en/4.2/ref/databases/#optimizing-postgresql-s-configuration


# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
# https://django-allauth.readthedocs.io/en/latest/installation.html?highlight=backends

# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#substituting-a-custom-user-model
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
# https://django-allauth.readthedocs.io/en/latest/views.html#logout-account-logout
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url

# https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware

# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS

# https://docs.djangoproject.com/en/dev/ref/settings/#templates
# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
# https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout

# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips



# |   Level               |   Numeric value   |
# |-------------------------------------------|
# | logging.CRITICAL      |       50          |
# | logging.ERROR         |       40          |
# | logging.WARNING       |       30          |
# | logging.INFO          |       20          |
# | logging.DEBUG         |       10          |
# | logging.NOTSET        |       0           |

# https://django-allauth.readthedocs.io/en/latest/configuration.html

# https://www.django-rest-framework.org/api-guide/settings/

# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration

# See more configuration options at https://drf-spectacular.readthedocs.io/en/latest/settings.html#settings


"""
