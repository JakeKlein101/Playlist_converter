import spotipy
from spotipy.oauth2 import SpotifyOAuth
from consts import *


def create_playlist(sp, playlist_name):
    sp.user_playlist_create(user=USERNAME, name=playlist_name, public=True, collaborative=False, description="")


def get_playlist_id(sp, playlist_name=""):
    playlists = sp.user_playlists(user=USERNAME, limit=50)
    for playlist in playlists["items"]:
        print(playlist["name"])
        if playlist["name"] == playlist_name:
            return playlist["id"]
    return 0


def main():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE,
                                                   client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=SPOTIPY_REDIRECT_URI))

    playlist_name = input("Whats the name of the playlist you want to create?")
    create_playlist(sp, playlist_name)
    playlist_id = get_playlist_id(sp, playlist_name)
    song_id = "spotify:track:1ANYHWUz5NqPu2EBALGK9Z"
    print(playlist_id)
    sp.playlist_add_items(playlist_id=playlist_id, items=[song_id])  # why?


if __name__ == '__main__':
    main()
