from django.views.generic import View

from .models import Release


class DownloadView(View):

    application = None

    def get(self, request, *args, **kwargs):
        # check for slug
        # check for version

        query = Release.objects.all()

        slug = getattr(kwargs, "slug", self.application)

        if slug is not None:
            query = query.filter(application__slug=slub)

        query = query.filter(version=kwargs['version'])

        return query.get()
