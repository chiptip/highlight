from core.models import Video
from rest_framework import serializers


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'source_url', 'duration', 'thumbnail_url', 'created')
        read_only_fields = ('id', 'title', 'duration', 'thumbnail_url', 'created')
