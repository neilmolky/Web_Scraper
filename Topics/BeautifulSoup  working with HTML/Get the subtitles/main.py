import requests

from bs4 import BeautifulSoup

index = int(input())
link = input()

r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")
subheadings = soup.find_all("h2")
subheading = subheadings[index]
print(subheading.get_text())
