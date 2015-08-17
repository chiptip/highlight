import numpy as np # for numerical operations
from moviepy.editor import VideoFileClip, concatenate
from core.models import Video

video = Video.objects.get(id=1)
print video.video.name

clip = VideoFileClip(video.video.name)
cut = lambda i: clip.audio.subclip(i,i+1).to_soundarray(fps=22000)
volume = lambda array: np.sqrt(((1.0*array)**2).mean())
volumes = [volume(cut(i)) for i in range(0,int(clip.duration-1))]

print 'volumes: %s' % volumes

averaged_volumes = np.array([sum(volumes[i:i+10])/10
                             for i in range(len(volumes)-10)])

print 'averaged_volumes: %s' % averaged_volumes

increases = np.diff(averaged_volumes)[:-1]>=0
decreases = np.diff(averaged_volumes)[1:]<=0
peaks_times = (increases * decreases).nonzero()[0]
peaks_vols = averaged_volumes[peaks_times]
peaks_times = peaks_times[peaks_vols>np.percentile(peaks_vols,90)]

print 'peaked: %s' % peaks_times

final_times=[peaks_times[0]]
for t in peaks_times:
    if (t - final_times[-1]) < 60:
        if averaged_volumes[t] > averaged_volumes[final_times[-1]]:
            final_times[-1] = t
    else:
        final_times.append(t)

print 'final: %s' % final_times

import matplotlib.pyplot as plt
# times = range(0,int(clip.duration-1))
# plt.plot(times, volumes)
times = range(len(volumes)-10)
plt.plot(times, averaged_volumes)

plt.xlabel("frames")
plt.ylabel("volumes")
plt.title("hello")
# plt.show()
plt.savefig("foo.png")

