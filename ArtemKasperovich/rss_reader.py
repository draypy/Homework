#!/usr/bin/python

import datetime
from bs4 import BeautifulSoup
import requests
from arg_parse import *
import json
import logging

class WrongUrl(Exception):
    pass

class Parser:
    def __init__(self):
        self.all_news = []
        self.version = 1.0
        self.feed_name = {}
        self.count = 0

    @staticmethod
    def output(data, limit=0):
        if limit:
            for news in data[:limit + 1]:
                for key, value in news.items():
                    print(key, ": ", value)
                print('\n')
        else:
            for news in data:
                for key, value in news.items():
                    print(key, ": ", value)
                print('\n')

    @staticmethod
    def verb(string, arg):
        if args.verbose:
            logger.info(f"{string}: {arg}")

    @staticmethod
    def get_response(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response
        raise WrongUrl
    @staticmethod
    def date_converter(date):
        keys = [
            "%a, %d %b %Y %H:%M:%S %z",
            '%Y-%m-%dT%H:%M:%SZ'
        ]
        for key in keys:
            try:
                date_obj = datetime.datetime.strptime(date, key)
                return date_obj.strftime("%a, %d %b %Y %H:%M:%S")
            except ValueError:
                pass

    def get_version(self):
        print(f'Version this programm is {self.version}')

    def parse_rss(self, response, limit=100000):
        soup = BeautifulSoup(response.content.decode().replace("\xa0", " ").replace("&nbsp;", " "), features='xml')
        if soup.find('rss'):
            self.feed_name['Feed'] = soup.title.text
            self.all_news.append(self.feed_name)
            items = soup.find_all('item')
            self.verb('Found news', len(items))
            if limit > len(items):
                limit = len(items)
            self.verb('Number of parsed news are ', limit)
            for item in items[:limit]:
                Title = item.title.text
                Date = self.date_converter(item.pubDate.text)
                try:
                    Link = item.link.text
                except AttributeError:
                    pass
                try:
                    Description = BeautifulSoup(item.description.text, 'lxml').get_text(strip=True)
                except AttributeError:
                    pass
                self.count += 1
                self.verb('News parsed', self.count)
                tags = ['Title', 'Link', 'Date', 'Description']
                current_news = {}
                for tag in tags:
                    try:
                        current_news[tag] = f'{eval(tag)}'
                    except NameError:
                        pass
                self.all_news.append(current_news)
            return self.all_news
        print('This url not a rss')

    def json(self):
        with open("json_data.json", 'w') as file:
            json.dump(self.all_news, file, indent=2, ensure_ascii=False)

    def main(self):
        try:
            url = args.source
            self.verb('Checking status code', url)
            resp = self.get_response(url)
            self.verb('Status code', int(resp.status_code))
            self.verb('Connection to', url)
            if args.limit:
                self.parse_rss(resp, args.limit)
                self.output(self.all_news, args.limit)
            else:
                self.parse_rss(resp)
                self.output(self.all_news)
            if args.json:
                parser.json()
                with open('json_data.json') as file:
                    print(file.read())

        except Exception:
            print('Wrong url')

        if args.version:
            try:
                self.get_version()
            except TypeError:
                pass


logging.basicConfig(format='%(message)s', level=logging.INFO)
logger = logging.getLogger()
logger.setLevel('INFO')

if __name__ == '__main__':
    parser = Parser()
    parser.main()
