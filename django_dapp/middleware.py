from typing import Optional

from django.apps import apps
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.utils.translation import ugettext_lazy as _
from rest_framework import status

from .models import Release


class MinimumVersionMiddleware:
    header_name = None

    def __init__(self, get_response):
        self.get_response = get_response
        self.header_name = apps.get_app_config('django_dapp').CHECK_VERSION_HEADER

    def __call__(self, request):
        request.app_release = None

        # check header
        response = self.check_version(request)
        if response is not None:
            return

        return self.get_response(request)

    def check_version(self, request: HttpRequest) -> Optional[HttpResponse]:
        """
        check_version checks if given version isn't older that minimum version
        :param request:
        :return:
        """

        header = request.META.get(self.header_name)

        if not header:
            return

        try:
            release, minimum = Release.objects.get_from_header(header)
        except ValueError as e:
            return HttpResponse(str(e), content_type="text/plain", status=status.HTTP_412_PRECONDITION_FAILED,
                                reason=str(e))

        request.app_release = release

        if minimum and release.version_info < minimum.version_info:
            reason = _("invalid version, minimum supported version is: {}, you are using {}, please update.").format(
                minimum.version, release.version,
            )

            return HttpResponse(reason, content_type="text/plain", status=status.HTTP_412_PRECONDITION_FAILED,
                                reason=reason)
        return
