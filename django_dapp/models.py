# -*- coding: utf-8 -*-
from __future__ import annotations

import hashlib
from typing import Optional

import semver
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class ApplicationManager(models.Manager):
    """
    Custom application manager
    """


class Application(TimeStampedModel):
    """
    Application
    """
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    description = models.TextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        get_latest_by = ['created']

    objects = ApplicationManager()

    def sorted_releases(self, reverse=False) -> [Release]:
        """
        sorted_releases returns sorted releases
        :return:
        """
        return sorted(list(Release.objects.all()), key=lambda x: semver.parse_version_info(x.version), reverse=reverse)

    def is_available_update(self, version: str) -> bool:
        """
        is_available_update returns if there is available update
        :param version:
        :return:
        """
        try:
            item = self.sorted_releases(reverse=True)[0]
        except IndexError:
            return False
        return semver.compare(item.version, version) > 0

    def is_supported(self, version: str) -> bool:
        """
        is_supported returns True if given version is higher or equal to minimum
        :param version:
        :return:
        """
        try:
            instance = Release.objects.filter(minimum=True)[0]
        except IndexError:
            return True

        return semver.compare(instance.version, version) <= 0

    def latest_release(self):
        """
        latest_release returns latest va browser release
        :return:
        """
        try:
            return self.sorted_releases(reverse=True)[0]
        except IndexError:
            return None

    def __str__(self):
        """
        String representation
        :return:
        """
        return '{}'.format(self.name)


class ReleaseManager(models.Manager):
    """
    Custom release manager
    """

    def get_from_header(self, header: str) -> [Release, Optional[Release]]:
        """
        get_release returns two releases
        first is release by given header, second is minimum release (if available)
        :return:
        """

        splitted = header.split("@", 1)
        if len(splitted) == 1:
            raise ValueError("invalid version header")

        try:
            release = self.get(application__slug=splitted[0], version=splitted[1])
        except self.model.DoesNotExist:
            raise ValueError("invalid version header")

        try:
            minimum = self.filter(application__slug=splitted[0], minimum=True)[0]
        except IndexError:
            minimum = None

        return release, minimum


def release_upload_to(instance, filename):
    """
    release_upload_to creates where to store file in media
    :param instance:
    :param filename:
    :return:
    """
    upload_to = str(apps.get_app_config("django_dapp").UPLOAD_TO).rstrip("/") + "/"
    return upload_to + filename


class Release(TimeStampedModel):
    """
    Release is application release
    """
    application = models.ForeignKey(Application, on_delete=models.PROTECT, related_name="releases")
    version = models.CharField(max_length=64)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    release_notes = models.TextField(blank=True)
    build = models.FileField(upload_to=release_upload_to)
    minimum = models.BooleanField(default=False)
    checksum = models.CharField(max_length=64, blank=True, default="")
    objects = ReleaseManager()

    class Meta:
        get_latest_by = ['created']

    def clean(self):
        """
        clean all fields
        :return:
        """
        try:
            version_info = semver.parse_version_info(self.version)
        except ValueError as e:
            raise ValidationError({"version", str(e)})

        try:
            latest_release = Release.objects.latest()
        except Release.DoesNotExist:
            latest_release = None

        if latest_release is not None:
            latest_version_info = latest_release.version_info
            if latest_version_info is not None:
                if latest_version_info >= version_info:
                    raise ValidationError({"version": _("please provide later version than in database")})

        # prepare checksum
        if self.build:
            checksum = hashlib.sha256()
            checksum.update(self.build.read())
            self.checksum = checksum.hexdigest()

    @property
    def version_info(self) -> Optional[semver.VersionInfo]:
        """
        version_info parses version and returns parsed VersionInfo
        :return:
        """
        try:
            return semver.parse_version_info(self.version)
        except ValueError:
            return None

    def save(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """

        super().save(*args, **kwargs)

        # check if we have set minimum version
        if self.minimum:
            Release.objects.filter(application=self.application).exclude(pk=self.pk).update(minimum=False)

    def __str__(self):
        """
        String representation
        :return:
        """
        return '{}@{}'.format(self.application, self.version)
