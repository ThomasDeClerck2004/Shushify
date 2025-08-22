import os
import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://127.0.0.1:8000/callback",
    scope="user-read-currently-playing"
))

def spotify_api():
    current_track = sp.current_user_playing_track()
    if current_track is not None and current_track['is_playing']:
        if current_track['currently_playing_type'] == 'ad':
            return True
        else:
            return False
    return False

def set_app_volume_low(app_name: str, is_ad: bool):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name().lower() == app_name.lower():
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if is_ad:
                volume.SetMasterVolume(0.0, None)  # Mute during ad
            else:
                volume.SetMasterVolume(1.0, None)  # Full volume otherwise

while True:
    is_ad = spotify_api()
    set_app_volume_low("Spotify.exe", is_ad)
    time.sleep(1)