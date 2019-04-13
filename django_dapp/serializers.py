from rest_framework import serializers

from .models import Release


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ('version', 'release_notes', 'checksum')
