from django.conf import settings
from rest_framework.request import HttpRequest
from datetime import datetime
from pathlib import Path


class RequestLoggingMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        with open(Path.joinpath(settings.BASE_DIR, 'requests.log'), "+a") as fd:
            fd.write(f"{datetime.now()} - User: {request.user} - Path: {request.path}\n")

        response = self.get_response(request)

        return response
