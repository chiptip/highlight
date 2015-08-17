from __future__ import unicode_literals
from cStringIO import StringIO
from highlight.settings import MEDIA_ROOT
import logging
import os
import sys
import youtube_dl


logger = logging.getLogger(__name__)

ORIG_VIDEO_DIR = "original"
ORIG_VIDEO_PATH = os.path.join(MEDIA_ROOT, ORIG_VIDEO_DIR)


class Capturing(list):
    '''
    quick utility class to capture stdout from
    youtube-dl program, it doesn't seem to just
    return output programmatically.
    '''
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


def download_video(url):
    ''' To download and extract filename '''

    opts = {
        'restrictfilenames': True,
        'outtmpl': ORIG_VIDEO_PATH + "/%(title)s.%(ext)s",
        'forcefilename': True,
        'forcetitle': True,
        'forcethumbnail': True,
        'forceduration': True,
        # 'forcedescription': True
    }

    # capture stdout into list of strings
    with Capturing() as output:
        with youtube_dl.YoutubeDL(opts) as ydl:
            ydl.download([url])

    # it should always be this element, if wrong, then need to loop
    # import pdb; pdb.set_trace()
    title = output[5]
    thumbnail_url = output[6]
    filename = output[7]
    duration = output[8]
    logger.debug('downloaded [%s] filename: [%s]' % (title, filename))
    return {
        'title': title,
        'thumbnail_url': thumbnail_url,
        'duration': duration,
        'filename': filename
    }
