from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = "pages/index.html"


class AboutPageView(TemplateView):  # new
    template_name = "pages/about.html"
