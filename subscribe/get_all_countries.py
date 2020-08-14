import re
import requests

from bs4 import BeautifulSoup

ALL_COUNTRIES = []

for column in BeautifulSoup(
        requests.get('https://history.state.gov/countries/all').text,
        'html.parser').find_all(
    'div', class_='col-md-6'):
    for div_box in column.find_all('div'):
        for item in div_box.find_all('a'):
            ALL_COUNTRIES.append(item.text)


def remove_symbols(country):
    country = re.sub("\(.*?\)", "", country)
    country = re.sub("[^A-Za-z-]+", "", country)
    return country


ALL_COUNTRIES = tuple(
    map(lambda x: (x.lower(), x.capitalize()), map(remove_symbols, ALL_COUNTRIES)))
