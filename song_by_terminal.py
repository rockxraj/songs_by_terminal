###################################
#
# Author Rajendra Gupta
#
####################################

import youtube_dl
import time
import vlc
import re
from gtts import gTTS
import os


instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
player = instance.media_player_new()

ydl_opts = {
    'default_search': 'ytsearch1:',
    # 'format': '249',
    'format': 'bestaudio/best',
    'noplaylist': True,
    'quiet': True
}

# Text to speech converter with translation


def say(words):
    tts = gTTS(text=words, lang='hi', slow=False)
    tts.save('welcome.mp3')
    os.system("cvlc "+'welcome.mp3 &')


def play_music(name):
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(name, download=False)
        # print(meta)
    except Exception:
        print('Sorry, I can\'t find that song.')
        return

    if meta:
        info = meta['entries'][0]
        say("now playing " + name)
        # mytext = "now playing " + name
        # myobj = gTTS(text=mytext, lang='hi', slow=False)
        # myobj.save("welcome.mp3")
        # os.system("cvlc welcome.mp3 &")
        # print(info['url'])
        media = instance.media_new(info['url'])

        player.set_media(media)
        print("\n------------------------------------------------\n")
        time.sleep(4)
        print('Now playing => ' + re.sub(r'[^\s\w]', '', info['title']) + '\n')
        player.play()


song = input("\nWrite song Name to play Music Or press 'q' To quit" +
             '\n' + '----------------------------\n')
if song == 'q':
    song = ''
    print("Youtube closed")
while song:
    play_music(song)
    song = input("Write song Name to play next song Or press 'q' To quit" +
                 '\n' + '----------------------------------\n')
    if song == 'q':
        song = ''
        print("Youtube closed")
