# Sync wall paper with bing

1- Place this project on /home/$USER/Pictures.

2- Put environment variables in a file to pass to crontab:

    env > ~/.cronenv && sed -i '/%s/d' ~/.cronenv

3- Set an entry in crontab table by `crontab -e`:

    */15 * * * * env $(cat ~/.cronenv | xargs) python3.8 /path/to/project/bing-wallpapers.py
