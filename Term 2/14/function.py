from bs4 import BeautifulSoup

import requests


def get(url):
    data = requests.get(url)
    return data

def make_soup(site):
    soup = BeautifulSoup(site.content, "html.parser")
    return soup

def get_tag(soup, t, c):
    tags = soup.find_all(t, class_=c)
    return tags
