from bs4 import BeautifulSoup

import requests


url = "https://divar.ir/s/rasht/bike-skate-scooter"
data = requests.get(url)
soup = BeautifulSoup(data.content, "html.parser")
names = soup.find_all('div', class_="kt-post-card__title")
prices = soup.find_all('div', class_="kt-post-card__top-description kt-post-card-description")
time = soup.find_all('span', class_="kt-post-card-description kt-post-card__bottom-description kt-text-truncate")
length = len(names)
for i in range(length):
    print(names[i].text, '>>>>>>', prices[i].text, '>>>>>>', time[i].text)