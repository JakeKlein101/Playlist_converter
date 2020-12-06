import spotify_handler
import youtube_handler


def main():
    query = youtube_handler.start_yt()
    spotify_handler.start_spotify(query)


if __name__ == '__main__':
    main()
