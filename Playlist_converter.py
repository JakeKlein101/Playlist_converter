import spotipy
from spotipy.oauth2 import SpotifyOAuth
from consts import *

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE,
                                               client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI))

sp.user_playlist_create(user=USERNAME, name="new new", public=True, collaborative=False, description="")
