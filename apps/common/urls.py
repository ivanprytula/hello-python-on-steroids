from django.urls import path

from apps.common import views

urlpatterns = [
    path("health-check/", views.health_check, name="health_check"),
    path("exception/", views.TriggerExceptionView.as_view(), name="exception"),
    path("email-admins/", views.EmailAdminsView.as_view(), name="email-admins"),
    path("version/", views.version, name="version"),
    path("db-conn-status/", views.db_connection_status, name="db-conn-status"),
]
