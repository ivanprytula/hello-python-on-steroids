from django.urls import path

from .views import AboutPageView, IndexPageView

app_name = "pages"
urlpatterns = [
    path("index/", IndexPageView.as_view(), name="index"),
    path("about/", AboutPageView.as_view(), name="about"),
]
