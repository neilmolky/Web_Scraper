import requests
import os
from bs4 import BeautifulSoup
from string import punctuation

def input_url():
    url = "https://www.nature.com/nature/articles"
    return url

def input_pages():
    print("enter the number of pages to scan: ", end="")
    valid_input = False
    while not valid_input:
        try:
            no_pages = int(input())
            valid_input = True
        except ValueError:
            print("Enter a number!")
    return no_pages


def input_type():
    print("enter the type of article to scan: ", end="")
    valid_input = False
    while not valid_input:
        art_type = input()
        return art_type


def find_articles(response, article_type):
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all('article')
    links = []
    for article in articles:
        if article.find('span', string=article_type):
            link = "https://www.nature.com"
            link += article.a.get('href')
            links.append(link)
    return links


def read_text(response):
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.find('div', {'class': 'c-article-body u-clearfix'})
    return text.text.strip()


def read_title(response):
    soup = BeautifulSoup(response.content, "html.parser")
    heading = soup.find('h1')
    title = heading.text.strip()
    title_table = title.maketrans(" ", "_", punctuation)
    return title.translate(title_table)


def web_response(url):
    r = requests.get(url)
    return r


def query(url, page):
    r = requests.get(
        url,
        params={'sort': 'PubDate', 'year': 2020, 'page': page}
    )
    return r


def web_content(url):
    return requests.get(url).content


def create_storage(directory, root):
    if (root and directory) in os.getcwd():
        print("already in this dir")
        return os.access(directory, os.W_OK)
    else:
        os.chdir(root)
    if directory in os.listdir(root):
        print("moving dir")
        os.chdir(directory)
    else:
        os.mkdir(directory)
        print("making dir")
        os.chdir(directory)
        print(os.getcwd())
    return os.access(os.getcwd(), os.W_OK)


def save_to_file(title, content, directory, root):
    if create_storage(directory, root):
        print("success")
        file = open(title+'.txt', 'wb')
        file.write(content)
        file.close()
        save_location = os.getcwd()
        return f"saved to {save_location}"
    else:
        return "directory error"


def main():
    root = os.getcwd()
    url = input_url()
    network_status = web_response(url)
    if network_status:
        search_list = {}
        pages = input_pages()
        page_counter = 0
        for p in range(pages):
            page_counter += 1
            search_list[page_counter] = query(url, page_counter)
        article_type = input_type()
        for page in search_list.keys():
            news = (find_articles(search_list.get(page), article_type))
            if news:
                for n in news:
                    directory = f"Page_{page}"
                    title = read_title(web_response(n))
                    text = read_text(web_response(n))
                    save_to_file(title, text.encode('UTF-8'), directory, root)
            else:
                directory = f"Page_{page}"
                create_storage(directory, root)
    else:
        print(f"The URL returned{network_status.status_code}")


if __name__ == "__main__":
    main()
