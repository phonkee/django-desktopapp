# -*- coding: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangoDappConfig(AppConfig):
    name = 'django_dapp'

    verbose_name = _('Desktop applications')

    # configuration
    CHECK_VERSION_HEADER = 'X-APP-VERSION'
    UPLOAD_TO = '/desktop-apps'

    def ready(self):
        """
        application is ready so we can read configuration
        :return:
        """

        from django.conf import settings

        config = getattr(settings, 'DJANGO_DAPP', {})

        self.UPLOAD_TO = getattr(config, 'UPLOAD_TO', self.UPLOAD_TO)
        self.CHECK_VERSION_HEADER = getattr(config, 'CHECK_VERSION_HEADER', self.CHECK_VERSION_HEADER)
