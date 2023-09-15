from django.urls import path

from apps.common import views

app_name = "common"

urlpatterns = [
    path("health-check/", views.health_check, name="health-check"),
    path("db-conn-status/", views.db_connection_status, name="db-conn-status"),
    path("project-version/", views.version, name="project-version"),
    path("test-exception/", views.TriggerExceptionView.as_view(), name="test-exception"),
    path("email-admins/", views.EmailAdminsView.as_view(), name="email-admins"),
]
