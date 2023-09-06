# from django.http import HttpResponse
from django.db import connection
from django.http import JsonResponse
from django.views.generic import TemplateView

# def home_page_view(request):
# return HttpResponse("Hello, World!")


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):  # new
    template_name = "pages/about.html"


def db_connection_status(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"message": "OK"}, status=200)
    except Exception as ex:
        return JsonResponse({"error": str(ex)}, status=500)
