from bs4 import BeautifulSoup
import requests

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the date: "))

link = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"
data = requests.get(link).text

soup = BeautifulSoup(data, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)