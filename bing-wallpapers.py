# coding: utf-8
import os
import subprocess
import requests
import json
import pwd

# CONSTANT
BASE_DIR = f'/home/{pwd.getpwuid(os.geteuid()).pw_name}/Pictures/bing-wallpaper'
BING = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'
CMD = 'gsettings set org.gnome.desktop.background picture-uri "file://{}"'


def check_new_image():
    r = requests.get(BING)
    j = json.loads(r.text)
    urlbase = j['images'][0]['urlbase']
    image_url = f"https://bing.com{urlbase}_1920x1080.jpg"
    filename = image_url.split('/')[-1]

    if filename not in os.listdir(BASE_DIR):
        image = requests.get(image_url)
        with open(os.path.join(BASE_DIR, filename), 'wb+') as f:
            f.write(image.content)
        image_path = os.path.abspath(os.path.join(BASE_DIR, filename))
        subprocess.Popen(CMD.format(image_path), shell=True)


if __name__ == '__main__':
    check_new_image()
