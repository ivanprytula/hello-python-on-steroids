from django.urls import path
from django.views.generic import TemplateView

from .views import AboutPageView, IndexPageView, index_page_view2, index_page_view3

app_name = "pages"
urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("fbv-index/", index_page_view2, name="fbv-index"),
    path("no-template/", index_page_view3, name="no-template"),
    path("no-app/", TemplateView.as_view(template_name="pages/index.html"), name="no-app"),
]
