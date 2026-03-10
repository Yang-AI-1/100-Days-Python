import requests
from bs4 import BeautifulSoup

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
#This gives me a static news page with titles and links.
#The titles are <a> tags

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser") #You pass in html code as the first argument.

articles = soup.find_all("a", class_="storylink")
article_titles = []
article_links = []
article_upvotes = [int(score.string.split()[0]) for score in soup.find_all("span",class_="score")]

for article_tag in articles:
    title = article_tag.string
    article_titles.append(title)
    link = article_tag.href
    article_links.append(link)

# print(article_titles)
# print(article_links)
# print(article_upvotes)

max_upvote = max(article_upvotes)
max_index = article_upvotes.index(max_upvote)
print(article_titles[max_index])
print(article_links[max_index])

