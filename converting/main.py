import os

import requests
from moviepy.editor import VideoFileClip

num = int
BASE_DIR = os.path.expanduser('~')
video_name = 'DownloadedTikTok.mp4'
filepath = os.path.join(BASE_DIR, video_name)
video_url = 'https://v16-webapp.tiktok.com/1bb5b6c9c84b0beee39f0e39d579a0af/62e92246/video/tos/useast2a/tos-useast2a' \
            '-pve-0068/a015cf81fcaf4d34a952a81e499e68a4/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br' \
            '=2216&bt=1108&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZwYJKwe2NNlwyl7Gb&mime_type=video_mp4&qs=0&rc' \
            '=ZzVnaWc7OmU1OzczNzQ6OkBpM3A1ZDk6Zmg2OzMzNzczM0AxXjVeMzVgXy0xNWEvXzUzYSM1bGkxcjQwYzBgLS1kMTZzcw%3D%3D&l' \
            '=202208020710190101902192041990925F '


def convert(url):
    resp = requests.get(url, video_name, allow_redirects=True)

    with open(filepath, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    videoClip = VideoFileClip(filepath)
    videoClip.write_gif(f'{BASE_DIR}/TikTokGif.gif')


convert(video_url)
