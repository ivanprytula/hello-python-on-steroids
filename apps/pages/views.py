from django.conf import settings
from django.shortcuts import HttpResponse, render
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = "pages/index.html"

    extra_context = {"BASE_URL": settings.ALLOWED_HOSTS[1], "BASE_PORT": 8000}


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


def index_page_view2(request):
    return render(request, "pages/index.html")


def index_page_view3(request):
    return HttpResponse("Hello World")
