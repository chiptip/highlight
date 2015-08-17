from __future__ import unicode_literals
from cStringIO import StringIO
from highlight.settings import MEDIA_ROOT
from moviepy.editor import VideoFileClip, concatenate
import logging
import matplotlib.pyplot as plt
import numpy as np # for numerical operations
import os
import sys
import youtube_dl


logger = logging.getLogger(__name__)

ORIG_VIDEO_DIR = "original"
ORIG_VIDEO_PATH = os.path.join(MEDIA_ROOT, ORIG_VIDEO_DIR)
ORIG_VOLUME_DIR = "original_volume"
ORIG_VOLUME_PATH = os.path.join(MEDIA_ROOT, ORIG_VOLUME_DIR)



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
        'video': os.path.join(ORIG_VIDEO_DIR,
                              os.path.basename(filename))
    }


def analyze_video(video_filename):
    video_fullpath = os.path.join(ORIG_VIDEO_PATH,
                                  os.path.basename(video_filename))
    clip = VideoFileClip(video_fullpath)
    cut = lambda i: clip.audio.subclip(i,i+1).to_soundarray(fps=22000)
    volume = lambda array: np.sqrt(((1.0*array)**2).mean())
    volumes = [volume(cut(i)) for i in range(0,int(clip.duration-1))]
    averaged_volumes = np.array([sum(volumes[i:i+10])/10 for i in range(len(volumes)-10)])
    # increases = np.diff(averaged_volumes)[:-1]>=0
    # decreases = np.diff(averaged_volumes)[1:]<=0
    # peaks_times = (increases * decreases).nonzero()[0]
    # peaks_vols = averaged_volumes[peaks_times]
    # peaks_times = peaks_times[peaks_vols>np.percentile(peaks_vols,90)]
    frames = range(0,int(clip.duration-1))
    plt.plot(frames, volumes)
    plt.xlabel("frames")
    plt.ylabel("volumes")
    image_filename = '%s.png' % os.path.basename(video_filename)[:-4]
    image_fullpath = os.path.join(ORIG_VOLUME_PATH, image_filename)
    image_relpath = os.path.join(ORIG_VOLUME_DIR, image_filename)
    try:
        logger.debug("image_fullpath: [%s]" % image_fullpath)
        plt.savefig(image_fullpath, transparent=True)
    except Exception, ex:
        logger.error("Failed to save image: [%s]" % image_fullpath)
        raise ex
    return image_relpath


def process_video(url):
    meta_data = download_video(url)
    meta_data['image'] = analyze_video(meta_data['video'])
    return meta_data
