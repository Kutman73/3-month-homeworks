from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests


URL = "https://www.securitylab.ru/news/"
link_url = "https://www.securitylab.ru"
photo = "https://www.securitylab.ru/"
HEADERS = {
    'ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.4.864 Yowser/2.5 Safari/537.36'
    }


def get_html(url, params=''):
    reg = requests.get(url=url, headers=HEADERS, params=params)
    return reg


def get_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('a', class_='article-card inline-card')
    news = []
    for item in items:
        news.append({
            'headline': item.find('div', class_='article-card-details').find('h2', class_='article-card-title').getText(),
            'link': link_url + item.get('href'),
            'data': item.find('div', class_='article-card-details').find('time').getText(),
        })
    return news


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        news = []
        for i in range(1, 2):
            html = get_html(f'{URL}page1_{i}.php')
            current_page = get_data(html.text)
            news.extend(current_page)
        return news
    else:
        raise Exception("Error in parser!")

