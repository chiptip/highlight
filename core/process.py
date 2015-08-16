from __future__ import unicode_literals
from core.models import ORIG_VIDEO_PATH
import logging
import youtube_dl


logger = logging.getLogger(__name__)


def video_download(url):
    ydl_opts = {
        'restrictfilenames': True,
        'outtmpl': ORIG_VIDEO_PATH + "/%(title)s.%(ext)s"
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
