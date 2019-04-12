# -*- coding: utf-8
from django.apps import AppConfig


class DjangoDappConfig(AppConfig):
    name = 'django_dapp'

    def ready(self):
        """
        application is ready so we can read configuration
        :return:
        """

        from django.conf import settings

        config = getattr(settings, 'DJANGO_DAPP', {})
        _ = config
