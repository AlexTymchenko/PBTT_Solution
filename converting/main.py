import os

import requests
from moviepy.editor import VideoFileClip

BASE_DIR = os.path.expanduser('~')
video_name = 'DownloadedTikTok.mp4'
filepath = os.path.join('/tmp', video_name)
video_url = 'https://v16-webapp.tiktok.com/ba5ce08b0cb58adad27a53d319c87841/62e97bfc/video/tos/maliva/tos-maliva-ve' \
            '-0068c799-us/3c242f508f5b4d77a6d4452d4ce81958/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1' \
            '&br=6220&bt=3110&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZWd1Kwe2NTS6yl7Gb&mime_type=video_mp4&qs=0&rc' \
            '=ODRmOjk0OjVlZzk1ZGg3ZkBpanR0cWQ6ZnNlOzMzZzczNEAxYjQvLjUvXjExYjJfMjYyYSMubDUvcjQwZWtgLS1kMS9zcw%3D%3D&l' \
            '=202208021333080101920560910F244222 '


def convert(url):
    resp = requests.get(url, video_name)
    if resp.status_code == 403:
        raise PermissionError('403 Forbidden. Url may be incorrect')

    with open(filepath, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    i = 0
    while os.path.exists(f'{BASE_DIR}/TikTokGif%s.gif' % i):
        i += 1

    videoClip = VideoFileClip(filepath)
    videoClip.write_gif(f'{BASE_DIR}/TikTokGif{i}.gif', fps=1)


convert(video_url)
