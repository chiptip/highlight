from core.models import Video
from rest_framework import serializers


class VideoSerializer(serializers.ModelSerializer):

    video_url = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    def get_video_url(self, obj):
        return obj.video.url

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Video
        fields = ('id', 'title', 'source_url', 'duration', 'created', 'thumbnail_url', 'video_url', 'image_url')
        read_only_fields = ('id', 'title', 'duration', 'created', 'thumbnail_url', 'video_url', 'image_url')
