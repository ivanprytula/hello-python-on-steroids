# from django.http import HttpResponse
from django.views.generic import TemplateView

# def home_page_view(request):
# return HttpResponse("Hello, World!")


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):  # new
    template_name = "pages/about.html"
