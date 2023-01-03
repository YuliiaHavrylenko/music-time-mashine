import requests
from bs4 import BeautifulSoup
import spotipy

CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"

OAUTH_AUTHORIZE_URL = 'http://example.com'

#------------------Authorize user in spotify------------------------------------
spotify_auth = spotipy.oauth2.SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=OAUTH_AUTHORIZE_URL,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
)
spotify_auth.get_access_token(as_dict=False)
s = spotipy.Spotify(oauth_manager=spotify_auth)
user_id = s.current_user()["id"]

#------------------Searching songs------------------------------------
date = input("Which year you want to travel? YYYY-MM-DD ")
year = date[:4]
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

billboard = response.text
soup = BeautifulSoup(billboard, "html.parser")
titles = soup.select(selector="li #title-of-a-story")
songs = [song.get_text().strip() for song in titles]
print(songs)

song_uris = []
for song in songs:
    result = s.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist i23n Spotify. Skipped.")


playlist = s.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
s.playlist_add_items(playlist_id=playlist["id"], items=song_uris)