import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# get request from the website

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html,"html.parser")
movies= soup.find_all(name="h3", class_="jsx-4245974604")
print(movies)

movie_titles = [movies.getText() for movie in movies]
