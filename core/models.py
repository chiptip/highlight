from core.process import video_download
from django.db import models
from highlight.settings import MEDIA_ROOT
import logging
import os

logger = logging.getLogger(__name__)
ORIG_VIDEO_DIR = "original"
ORIG_VIDEO_PATH = os.path.join(MEDIA_ROOT, ORIG_VIDEO_DIR)


# Create your models here.
class VideoManager(models.Manager):

    def create(self, source_url):

        # do something with the video
        logger.debug("Downloading URL: %s" % source_url)
        video_download(source_url)

        # actual instantiate the video object
        video = Video(source_url=source_url)
        video.save()

        return video


class Video(models.Model):
    name = models.CharField(max_length=100)
    source_url = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to=ORIG_VIDEO_DIR)

    objects = VideoManager()

    class Meta:
        ordering = ('created',)


