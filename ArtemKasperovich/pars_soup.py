# from bs4 import BeautifulSoup
# import requests
from datetime import datetime as dt
import argparse
parser1 = argparse.ArgumentParser(description='Pure Python command-line RSS reader.')
parser1.add_argument('source', help='RSS URL')
parser1.add_argument("--version", metavar='', help='Print version info')
parser1.add_argument("--json", metavar='', help="Print version JSON in stdout")
parser1.add_argument("--verbose", metavar='', help="Outputs verbose status messages")
parser1.add_argument("--limit", help="Limit new topics if parameter provided", type=int)


#
URL1 = "https://people.onliner.by/feed"
URL2 = "https://www.thecipherbrief.com/feed"
URL3 = 'https://news.yahoo.com/rss/'
URL4 = 'https://rss.art19.com/apology-line'
URL5 = 'https://news.un.org/feed/subscribe/ru/news/region/europe/feed/rss.xml'
URL6 = 'http://avangard-93.ru/news/rss'
URL7 = 'http://avangard-93.ru/news/rss'
URL8 = 'http://www.forbes.com/most-popular/feed/'
# # URL = input('Enter a link: ')
#
# response = requests.get(URL)
# soup = BeautifulSoup(response.text, features='xml')
# main_title = soup.title.text
# print("Feed: ", main_title)
# items = soup.find_all('item')
# all_news = []
# for item in items:
#     title = item.title.text
#     link = item.link.text
#     pubDate = item.pubDate.text
#     description = BeautifulSoup(item.description.text, 'lxml').text
#     print(f'Title: {title}', f'link: {link}', f'Date: {pubDate}', f'Description: {description}', sep='\n')
#
