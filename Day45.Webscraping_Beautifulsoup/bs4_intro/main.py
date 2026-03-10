from bs4 import BeautifulSoup

with open("./website.html") as webfile:
    contents = webfile.read()

soup = BeautifulSoup(contents, "html.parser")
