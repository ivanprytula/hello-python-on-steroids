"""
Wrapping API views

1. The @api_view decorator for working with function based views.
2. The APIView class for working with class-based views.
3. Using mixins
4. Using generic class-based views
5. ViewSets & Routers

"""

from django.conf import settings
from django.db import connection
from django.http import JsonResponse

from loguru import logger

# from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CustomSerializer
from .tasks import send_email_debug_task


def health_check(request):
    return JsonResponse({"message": "OK"})


def db_connection_status(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"message": "SELECT 1 - OK"}, status=200)
    except Exception as ex:
        return JsonResponse({"error": str(ex)}, status=500)


def version(request):
    return JsonResponse({"version": settings.SOURCE_TAG, "foo": "bar"})


# @api_view(["POST"])
# @authentication_classes([])
# @permission_classes([])
# def trigger_exception(request):
#     """
#     Triggers an exception. used for testing
#     """
#     raise APIException("Exception message from the API server")


class TriggerExceptionView(APIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = None

    def post(self, request):
        """
        Triggers an exception. used for testing
        """
        logger.debug(request)
        raise APIException("Exception message from the API server")


# ----- FBV style ------
# @api_view(["POST"])
# @authentication_classes([])
# @permission_classes([])
# def email_admins(request):
#     send_email_debug_task.apply_async()
#     return JsonResponse({"message": "Email sent!"})

# ----- CBV style ------


class EmailAdminsView(APIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = CustomSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Calling .save() will either create a new instance,
            # or update an existing instance, depending on if an existing instance was passed
            # when instantiating the serializer class
            data = serializer.save()
            # process the data as needed
            send_email_debug_task.apply_async()
            return Response({"message": "Data processed! Email sent!", "data": data})

        logger.error(request)
        return Response(serializer.errors, status=400)
