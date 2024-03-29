# django-step-by-step (c) 2023 Brian Caffey
# https://github.com/briancaffey/django-step-by-step/blob/main/backend/apps/core/middleware.py

import logging
import time

from apps.common.models import RequestLog

logger = logging.getLogger(__name__)


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        response_ms = duration * 1000
        path = request.path
        if "health-check" in path:
            return response

        user = None
        if request.user.is_authenticated:
            user = request.user
        full_path = request.get_full_path()
        method = str(getattr(request, "method", "")).upper()
        remote_address = self.get_client_ip(request)
        response_code = response.status_code

        request_log = RequestLog(
            user=user,
            path=path,
            full_path=full_path,
            execution_time=response_ms,
            response_code=response_code,
            method=method,
            remote_address=remote_address,
        )

        request_log.save()

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.headers.get("x-forwarded-for")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")
