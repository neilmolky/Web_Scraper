import requests

from bs4 import BeautifulSoup

user_input_1 = input()
user_input_2 = input()
try:
    act = int(user_input_1)
    link = requests.get(user_input_2)
except ValueError:
    act = int(user_input_2)
    link = requests.get(user_input_1)

if link:
    soup = BeautifulSoup(link.content, "html.parser")
    links = soup.find_all("a")
    choice = links[act - 1]
    print(choice.get("href"))

