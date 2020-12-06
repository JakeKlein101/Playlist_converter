from youtube_consts import *
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


def create_title_list(response):
    ret_list = []
    for item in response["items"]:
        ret_list.append(item["snippet"]["description"])
        print(item["snippet"]["title"])  # TODO: Parse by description.
    return ret_list


def connect_and_auth_api():
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name,
                                              api_version,
                                              credentials=credentials)
    return youtube


def get_playlist_from_api(youtube):
    request = youtube.playlistItems().list(part="snippet", playlistId=TEST_PLAYLIST)
    response = request.execute()
    return response


def parse_title_list_to_query(titles_list):
    query_list = []
    temp_list = []
    for title in titles_list:
        temp_list = title.split(" - ")
        artist_name = temp_list[0]
        song_name = temp_list[1]
        if "ft" in song_name:
            ft_index = temp_list[1].find("ft")
            song_name = temp_list[1][:ft_index]
        if "(Official Music Video)" in temp_list[1]:
            song_name = song_name.strip("(Official Music Video)")
        query = artist_name + "%" + song_name
        print(query)
        query_list.append(query)
    return query_list


def start_yt():
    # youtube = connect_and_auth_api()
    # response = get_playlist_from_api(youtube)
    titles_list = create_title_list(test_rep)
    return parse_title_list_to_query(titles_list)


def main():
    start_yt()


if __name__ == '__main__':
    main()
