import io
from os import environ
from tkinter import *
from PIL import Image, ImageTk
import urllib.request

import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = environ['SPOTIFY_CLIENT_ID']
client_secret = environ['SPOTIFY_CLIENT_SECRET']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri='http://localhost:8888/callback',
                                               scope="user-read-currently-playing"))

window = Tk()
window.overrideredirect(True)
window.overrideredirect(False)  # For MacOS
# window.attributes('-fullscreen', True)
window.wm_attributes("-topmost", True)
window.geometry("+64+64")
display1 = Label(window)
display1.grid(row=1, column=0, padx=0, pady=0)


def show_frame():
    track = sp.current_user_playing_track()['item']
    album_cover = track['album']['images'][0]['url']

    raw_data = urllib.request.urlopen(album_cover).read()
    img = Image.open(io.BytesIO(raw_data))
    img_tk = ImageTk.PhotoImage(img)
    display1.imgtk = img_tk
    display1.configure(image=img_tk)

    # https://stackoverflow.com/questions/46322838/any-ideas-about-rate-limit-request-minute-on-spotify-api
    window.after(1000, show_frame) # run show_frame() every 500 ms


show_frame()
window.mainloop()
