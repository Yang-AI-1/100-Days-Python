from bs4 import BeautifulSoup
import requests

#TODO.1) Scraping logic.
# Make a get request to obtain the html website data
# Create a soup object of the contents.
# Access the names of the titles from the webpage in list format.
empire_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(empire_url)
response.raise_for_status()
empire_html = response.text
soup = BeautifulSoup(empire_html,"html.parser") #specify the html parser.

movie_titles = [title.string for title in soup.find_all(name="h3", class_="title")]

#TODO.2) Data editing and storage logic.
# Invert the contents of the list.
# Store the data in a text file one by one.

movie_titles.reverse() #It reverses the movie titles in memory. That's so cool.

with open("movies.txt","a",encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(movie + "\n")

