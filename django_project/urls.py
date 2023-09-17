# flake8: noqa

"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic.base import TemplateView

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

# https://adamj.eu/tech/2022/11/24/django-settings-patterns-to-avoid/
# TIP: Don’t Read Settings at Import Time - Do it at run time!
#  Python doesn’t make a distinction between import time and run time.
#  As such, it’s possible to read settings at import time, but this can lead to subtle bugs.
#  Reading a setting at import time will use or copy its initial value, and will not account for any later changes.
#  Settings don’t often change, but when they do, you definitely want to use the new value.

urlpatterns = [
    path("", include("apps.pages.urls", namespace="pages")),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("apps.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    # https://adamj.eu/tech/2020/02/10/robots-txt/
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]


# API URLS
api_version = "api"

urlpatterns += [
    # health check, exception, email-admins
    path(f"{api_version}/", include("apps.common.urls", namespace="common")),
    # API base url for ViewSets-based apps
    path(f"{api_version}/", include("django_project.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
    path(f"{api_version}/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        f"{api_version}/schema/swagger-ui",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="swagger-ui",
    ),
    path(
        f"{api_version}/schema/redoc/",
        SpectacularRedocView.as_view(url_name="api-schema"),
        name="redoc",
    ),
]

# static files
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]

    # https://127.0.0.1:8000/api-auth/login/?next=/api/v1/
    urlpatterns += [path("api-auth/", include("rest_framework.urls"))]

    # django-silk
    urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
