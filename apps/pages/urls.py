from django.urls import path

from .views import AboutPageView, HomePageView, db_connection_status

app_name = "pages"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("status/", db_connection_status, name="status"),
]
