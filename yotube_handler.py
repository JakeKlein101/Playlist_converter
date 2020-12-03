from youtube_consts import *
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name,
                                              api_version,
                                              credentials=credentials)

    request = youtube.playlistItems().list(part="snippet", playlistId=TEST_PLAYLIST)
    response = request.execute()

    for item in response:
        print(item["items"]["title"])


if __name__ == '__main__':
    main()
