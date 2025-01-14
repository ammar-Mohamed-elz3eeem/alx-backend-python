from django.conf import settings
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from pathlib import Path
from rest_framework.renderers import JSONRenderer


class RequestLoggingMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        with open(Path.joinpath(settings.BASE_DIR, 'requests.log'), "+a") as fd:
            fd.write(f"{datetime.now()} - User: {request.user} - Path: {request.path}\n")

        response = self.get_response(request)

        return response


class RestrictAccessByTimeMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        current_hour = datetime.now().hour

        if current_hour < 9 or current_hour > 18:
            response = Response(data="Forbidden Access to App outside 9AM to 6PM", status=HTTP_403_FORBIDDEN)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = 'application/json'
            response.renderer_context = {}
            response.render()
            return response

        response: Response = self.get_response(request)

        return response


class OffensiveLanguageMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_tracker = {}

    @staticmethod
    def get_client_ip(request):
        http_x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if http_x_forwarded_for:
            return http_x_forwarded_for.split(",")[-1]
        return request.META.get("REMOTE_ADDR")

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)

        if request.method == 'POST' and "/messages/" in request.path:
            ip = self.get_client_ip(request)
            current_time = datetime.now()
        else:
            return response

        if ip not in self.requests_tracker:
            self.requests_tracker[ip] = {'count': 1, 'start_time': current_time}
        else:
            data = self.requests_tracker[ip]
            elapsed_time = current_time - data.start_time

        if elapsed_time > timedelta(minutes=1):
            self.requests_tracker[ip] = {'count': 1, 'start_time': current_time}
        else:
            if data['count'] > 5:
                response = Response(data={
                    "error": "Message rate limit exceeded, Try again later."
                }, status=status.HTTP_429_TOO_MANY_REQUESTS)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'application/json'
                response.renderer_context = {}
                response.render()
                return response
            self.requests_tracker[ip]['count'] += 1

        return response


class RolePermissionMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        protected_paths = ["/admin/", "/messages/"]
        if any([path in request.path for path in protected_paths]):
            print("Authenticated user", request.user.role)
            if request.user.role not in ['admin', 'host']:
                response = Response(data={
                    "error": "Only allowed for loggedin users"
                }, status=status.HTTP_429_TOO_MANY_REQUESTS)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'application/json'
                response.renderer_context = {}
                response.render()
                return response
        response = self.get_response(request)
        return response
