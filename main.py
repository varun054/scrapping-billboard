import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
CLIENT_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_KEY,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Varun", 
    )
)
user_id = sp.current_user()["id"]

# Scrap top 100 song titles from billboard website.
year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
url = f"https://www.billboard.com/charts/hot-100/{year}"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, "html.parser")
top_100_songs = soup.select(".lrv-u-width-100p > ul > li > h3")
song_names = [song.getText().strip() for song in top_100_songs]
print(song_names)
