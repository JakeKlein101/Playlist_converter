import spotipy
from spotipy.oauth2 import SpotifyOAuth
import applemusicpy
import Spotify_consts


def create_playlist(sp, playlist_name):
    sp.user_playlist_create(user=Spotify_consts.USERNAME,
                            name=playlist_name, public=True,
                            collaborative=False,
                            description=input("Describe your playlist:"))


def get_playlist_id(sp, playlist_name=""):
    playlists = sp.user_playlists(user=Spotify_consts.USERNAME, limit=50)
    for playlist in playlists["items"]:
        if playlist["name"] == playlist_name:
            return playlist["id"]
    return 0


def get_song_id_list_by_names(sp):
    song_id_list = []
    song_names_list = ["franchise", "90210", "heartless"]
    for song in song_names_list:
        searched = sp.search(q=song, type="track", market="IL", limit=1)
        song_id_list.append(searched["tracks"]["items"][-1]["uri"])
    return song_id_list


def start_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=Spotify_consts.SCOPE,
                                                   client_id=Spotify_consts.CLIENT_ID,
                                                   client_secret=Spotify_consts.CLIENT_SECRET,
                                                   redirect_uri=Spotify_consts.SPOTIPY_REDIRECT_URI))

    playlist_name = input("Whats the name of the playlist you want to create?")
    create_playlist(sp, playlist_name)
    playlist_id = get_playlist_id(sp, playlist_name)
    song_id_list = get_song_id_list_by_names(sp)
    sp.playlist_add_items(playlist_id=playlist_id, items=song_id_list)


def main():
    pass


if __name__ == '__main__':
    main()
