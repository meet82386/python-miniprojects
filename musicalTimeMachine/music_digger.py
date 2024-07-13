from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# year = int(input("Enter the year: "))
# month = int(input("Enter the month: "))
# day = int(input("Enter the date: "))
year, month, day = 2012, 12, 12

link = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"
data = requests.get(link).text

soup = BeautifulSoup(data, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)


with open("data.txt") as file:
    id=file.readline().split("=")[1].strip()
    sec=file.readline().split("=")[1].strip()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://google.com",
        client_id=id,
        client_secret=sec,
        show_dialog=True,
        cache_path="token.txt",
        username="meet", 
    )
)
user_id = sp.current_user()["id"]
print(user_id)