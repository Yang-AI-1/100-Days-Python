import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
try:
    music_year = int(input("Which year do you want to travel to? Type the data in the format YYYY\n"))
except Exception:
    print("Kinly type appropriate year in number format")
else:
    #Request for website html data.
    header = {"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"}
    billboard_endpoint = f"https://www.billboard.com/charts/year-end/{music_year}/hot-100-songs/"
    response = requests.get(url=billboard_endpoint,headers=header)
    response.raise_for_status()
    web_data = response.text

    #Parse with beautiful soup.
    soup = BeautifulSoup(web_data,"html.parser")
    top_100 = [song.get_text(strip=True) for song in soup.select(".chart-results-list h3.c-title[id='title-of-a-story']")]

    #Spotipy authentication by creating spotify client.
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                   client_secret=SPOTIFY_CLIENT_SECRET,
                                                   redirect_uri= "https://example.com",
                                                   scope="playlist-modify-private"))
    #Searching for songs and obtaining song_URI's used as the song identifiers.
    song_uri_list = []
    for song in top_100:
        result = sp.search(q=song, type="track", limit=1)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uri_list.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    #
    playlist = sp.current_user_playlist_create(name=f"{music_year} Billboard 100",public=False)
    playlist_id = playlist["id"]
    sp.playlist_add_items(playlist_id=playlist_id,items=song_uri_list)