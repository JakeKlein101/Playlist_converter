# Playlist_converter
A program to convert apple music/youtube playlists to Spotify playlists
## Usage

```python
import spotify_handler
import youtube_handler


def main():
    query = youtube_handler.start_yt()
    spotify_handler.start_spotify(query)
```
