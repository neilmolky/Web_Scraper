import requests

from bs4 import BeautifulSoup

article = input()

r = requests.get(article)
soup = BeautifulSoup(r.content, "html.parser")

heading = soup.find("h1")
print(heading.get_text())