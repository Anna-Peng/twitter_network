import requests
from bs4 import BeautifulSoup

URL = requests.get('https://www.zdnet.com/article/directory-100-technology-experts-on-twitter/')


def scrape_experts():
    soup = BeautifulSoup(URL.text, 'html.parser')
    names = []
    user_names = []
    for ol in soup.find_all('ol'):
        for x in ol.find_all('strong'):
            names.append(x.get_text())
        for x in ol.find_all('a', href=True):
            user_names.append(x.get_text())

    return user_names
