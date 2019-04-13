import semver
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Application
from .models import Release
from .serializers import ReleaseSerializer


class DownloadView(View):
    application_slug = ""

    def get(self, request, *args, **kwargs):
        obj = self.get_object(request, *args, **kwargs)
        filename = obj.build.name.split('/')[-1]
        response = HttpResponse(obj.build, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response

    def get_object(self, request, *args, **kwargs):
        # check for slug
        # check for version

        query = Release.objects.all()

        application_slug = getattr(kwargs, "application_slug", self.application_slug)

        if application_slug:
            query = query.filter(application__slug=application_slug)

        query = query.filter(version=kwargs['version'])

        return query.get()


class VersionUpdateView(View):
    application_slug = None

    def get(self, request, *args, **kwargs):
        """
        get http request
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            version_info = semver.parse_version_info(kwargs.get("version", None))
        except ValueError:
            raise Http404

        # get latest release so we can compare versions
        latest_release = self.get_latest_release(request, *args, **kwargs)

        if latest_release.version_info > version_info:
            serializer = ReleaseSerializer(latest_release)
            return Response(serializer.data, status=HTTP_200_OK)

        raise Http404

    def get_latest_release(self, request, *args, **kwargs):
        """
        get_latest_release returns latest application release
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        application_slug = kwargs.get("application_slug", self.application_slug)

        assert application_slug is None, "Application slug was not provided!"

        try:
            application = Application.objects.get(slug=application_slug)
        except Application.DoesNotExist:
            raise

        return application.latest_release()
