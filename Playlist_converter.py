import spotipy
from spotipy.oauth2 import SpotifyOAuth
from consts import *

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE,
                                               client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI))

playlist_name = "new new"
playlist_id = 0
sp.user_playlist_create(user=USERNAME, name=playlist_name, public=True, collaborative=False, description="")
playlists = sp.user_playlists(user=USERNAME, limit=50)
for playlist in playlists["items"]:
    if playlist["name"] == playlist_name:
        playlist_id = playlist["id"]
        break
sp.playlist_add_items(playlist_id=playlist_id, items="spotify:track:2hiuiI3ac0I5kJWtkeGHEL", position=1)  # why?
