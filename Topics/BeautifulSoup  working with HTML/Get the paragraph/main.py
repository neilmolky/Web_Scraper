import requests
from bs4 import BeautifulSoup

word = input()
link = input()

r = requests.get(link)
if r:
    soup = BeautifulSoup(r.text, "html.parser")
    paragraphs = soup.findAll("p")
    for p in paragraphs:
        if word in p.text:
            print(p.text)
            break
