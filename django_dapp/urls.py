from django.urls import path

from .views import VersionUpdateView, DownloadView


def get_api_urls(slug=None):
    """
    get_api_urls returns proper urls to be included
    :param slug: if given, we generate urls only for single application
    :return:
    """

    if slug is not None:
        return [
            path("<version>/update/", VersionUpdateView.as_view(application_slug=slug), name=slug + "-version"),
            path("<version>/download/", DownloadView.as_view(application_slug=slug), name=slug + "-download"),
        ]

    return [
        path("<application_slug>/update/<version>/", VersionUpdateView.as_view()),
    ]
