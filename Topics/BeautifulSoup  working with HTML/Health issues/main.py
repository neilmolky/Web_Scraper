import requests

from bs4 import BeautifulSoup

url = input()
letter = "S"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
anchors = soup.find_all('a')
topics = []

for anchor in anchors:
    href = anchor.get('href')
    if href and ('topics' in href or 'entity' in href):
        text = anchor.text
        if text and len(text) > 1 and text.startswith(letter):
            topics.append(anchor.text)

print(topics)