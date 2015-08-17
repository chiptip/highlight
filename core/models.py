from core.process import download_video, ORIG_VIDEO_DIR,\
                         ORIG_VIDEO_DIR
from django.core.files import File
from django.db import models
import logging

logger = logging.getLogger(__name__)


# Create your models here.
class VideoManager(models.Manager):

    def create(self, source_url, name=None):

        # do something with the video
        logger.debug("Downloading URL: %s" % source_url)
        meta = download_video(source_url)

        # actual instantiate the video object
        video = Video(title=meta['title'],
                      source_url=source_url,
                      duration=meta['duration'],
                      thumbnail_url=meta['thumbnail_url'])
        video.video.name = meta['filename']
        video.save()
        return video


class Video(models.Model):
    title = models.CharField(max_length=100)
    source_url = models.CharField(max_length=255)
    duration = models.CharField(max_length=10)
    thumbnail_url = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to=ORIG_VIDEO_DIR)

    objects = VideoManager()

    class Meta:
        ordering = ('-created',)


