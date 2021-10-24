import datetime
from bs4 import BeautifulSoup
import requests
import argparse
import json
import logging
import os
import glob


class Parser:
    def __init__(self):
        self.today_parsed_news = []
        self.feed_name = {}
        self.count_news = 0
        self.logger = logging.getLogger()
        self.local_cache = []

    @staticmethod
    def get_response(url: str) -> requests.Response:
        try:
            response = requests.get(url)
            return response
        except requests.RequestException:
            print('Something went wrong! Please check the link')

    @staticmethod
    def date_converter(date: str) -> datetime.datetime.strftime:
        keys = [
            "%a, %d %b %Y %H:%M:%S %z",
            '%Y-%m-%dT%H:%M:%SZ',
            "%a, %d %b %Y %H:%M:%S %Z"
        ]
        for key in keys:
            try:
                date_obj = datetime.datetime.strptime(date, key)
                return date_obj.strftime("%a, %d %b %Y %H:%M:%S")
            except ValueError:
                pass

    def get_news_by_date(self, date):
        convert_date = datetime.datetime.strptime(date, '%Y%m%d')
        pretty_date = convert_date.strftime("%a, %d %b %Y")
        for filepath in glob.glob(os.path.join('data_cache', '*.json')):
            with open(filepath) as content:
                data = json.load(content)
                for news in data:
                    for key in news.keys():
                        if pretty_date in news[key]:
                            self.local_cache.append(news)

    def output(self, news: list = None, limit: int = None, date: str = None):
        self.logger.info('Start printing...')
        if news is None:
            news = self.today_parsed_news
        if args.date:
            news = self.local_cache
        if args.limit:
            limit = args.limit
        if limit is not None:
            if args.json:
                print(json.dumps(news[:limit], indent=2, ensure_ascii=False))
                return
            for new in news[-limit:]:
                for tag, tag_value in new.items():
                    print(tag, ": ", tag_value)
                print()
            self.today_parsed_news.clear()
            self.local_cache.clear()
        else:
            if args.json:
                print(json.dumps(news, indent=2, ensure_ascii=False))
                return
            for new in news:
                for tag, tag_value in new.items():
                    print(tag, ": ", tag_value)
                print()
            self.today_parsed_news.clear()

    def json_cache(self, news: dict):
        try:
            with open(f"data_cache/{self.feed_name['Feed']}.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        if news not in data:
            data.append(news)
        with open(f"data_cache/{self.feed_name['Feed']}.json", 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def get_tag_content(self, item) -> dict:
        current_news = {}
        tags = ['title', 'link', 'pubDate', 'description']
        for tag in tags:
            for tag_content in item.contents:
                if tag == tag_content.name:
                    if tag_content.name == 'description':
                        current_news[tag.capitalize()] = BeautifulSoup(tag_content.text, 'lxml').get_text(strip=True)
                    elif tag_content.name == 'pubDate':
                        current_news[tag.capitalize()] = self.date_converter(tag_content.text)
                    else:
                        current_news[tag.capitalize()] = tag_content.text
        return current_news

    def parse_rss(self, response: requests.Response):
        self.logger.info('Start parsing')
        soup = BeautifulSoup(response.content.decode().replace("\xa0", " ").replace("&nbsp;", " "), features='xml')
        self.logger.info('Check rss link or not')
        if soup.find('rss'):
            self.feed_name['Feed'] = soup.title.text
            self.json_cache(self.feed_name)
            self.today_parsed_news.append(self.feed_name)
            items = soup.find_all('item')
            for item in items:
                self.json_cache(self.get_tag_content(item))
                self.today_parsed_news.append(self.get_tag_content(item))
                self.count_news += 1
                self.logger.info(f'News parsed: {self.count_news}')

        else:
            print('This not a rss link')

    def read_file(self, date: str, limit: int = None):
        convert_date = datetime.datetime.strptime(date, '%Y%m%d')
        pretty_date = convert_date.strftime("%a, %d %b %Y")
        self.logger.info(f'Convert {date} to human readable view: {pretty_date}')
        self.logger.info('Checking cached news')
        for filepath in glob.glob(os.path.join('data_cache', '*.json')):
            with open(filepath) as content:
                data = json.load(content)
                for news in data:
                    for key in news.keys():
                        if pretty_date in news[key]:
                            self.local_cache.append(news)

    def read_url(self, date: str):
        convert_date = datetime.datetime.strptime(date, '%Y%m%d')
        pretty_date = convert_date.strftime("%a, %d %b %Y")
        self.logger.info(f'Convert {date} to human readable view: {pretty_date}')
        for news in self.today_parsed_news:
            for key in news.keys():
                if pretty_date in news[key]:
                    self.local_cache.append(news)

    def run_parse(self):
        url = args.source
        self.logger.info(f'Checking status code {url}')
        resp = self.get_response(url)
        self.logger.info(f'Status code = {int(resp.status_code)}')
        self.logger.info(f'Connection to {url}')
        self.parse_rss(resp)


parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader.')
parser.add_argument('source', help='RSS URL', nargs='?')
parser.add_argument("--version", help='Print version info', action='version', version='version 3.0')
parser.add_argument("--json", action='store_true', help="Print version JSON in stdout")
parser.add_argument("--verbose", action='store_true', help="Outputs verbose status messages")
parser.add_argument("--limit", help="Limit new topics if parameter provided", type=int)
parser.add_argument("--date", help="Output news output by date", type=str)
args = parser.parse_args()


def main():
    pars = Parser()
    if args.verbose:
        logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING,
                            format='%(message)s')
    if args.source:
        pars.run_parse()
        if args.date:
            pars.read_url(args.date)
            pars.output()

        else:
            pars.output()
    else:
        if args.date:
            pars.read_file(args.date, args.limit)
            pars.output()


if __name__ == '__main__':
    main()
