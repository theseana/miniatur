from function import get, make_soup, get_tag


url = "https://divar.ir/s/rasht/bike-skate-scooter"

s = get(url)
soop = make_soup(s)
tags = get_tag(soop, 'div', 'kt-post-card__top-description kt-post-card-description')
for tag in tags:
    print(tag)