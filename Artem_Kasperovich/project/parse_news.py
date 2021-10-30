"""
Module containing the core logics.
"""
from datetime import datetime
from typing import List, Optional
import bs4
import json
import logging
import os
import re
import requests

PATH = html_path = os.path.join(os.path.dirname(__file__), "news_cache", "news.json")


class ParserError(requests.exceptions.ConnectionError, ValueError, AttributeError):
    """
    A class for catching and reading human readable errors
    """
    pass


class NewsParser:
    """ Class that parsing site and write result in news.json file
            in format, which the user specified.
        Attributes:
            url: url of rss file
            limit: limit of news when printing an object
            json_format: printing in json format (true, False)
            date: date of the searching news
    """

    def __init__(self,
                 url: str = None,
                 limit: int = None,
                 json_format: bool = False,
                 date: str = None):
        self.logger = logging.getLogger(__name__)
        self.logger.info("Start constructor")
        self.url = url
        self.limit = limit
        self.json_format = json_format
        self.json_link = PATH
        self.response = None
        self.items_dict = {}
        self.date = date
        self.logger.info("End constructor")

    def parse(self):
        """
        Runs the script depending on the command line arguments
        :return:
        """
        if self.date is not None:
            self.date = self._arg_date_check()
        if self.url:
            self.response = self.get_response(self.url)
            self.logger.info("Create json file and dict with information!")
            self.items_dict = self.parsing_rss(self.response)
        else:
            self.logger.info("Create json file and dict with information!")
            self.items_dict = self.read_json()
        self.limit = len(self.items_dict["items"]) \
            if self.limit is None else abs(self.limit)

    @staticmethod
    def get_response(url: str) -> requests.Response:
        """
        Getting response and checked status code
        :param url: The received url
        :return:
        """
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response
        except requests.RequestException:
            print('Please check your entered link')
            raise ParserError

    def parsing_rss(self, response: requests.Response) -> dict:
        """Parses the rss page according to the given url
        :param response:
        :return: dict with information
        """
        self.logger.info(f"Start parse {self.url}")
        soup = bs4.BeautifulSoup(response.content, features='xml')
        if not soup.find('rss'):
            print('THis is not a rss link')
            raise ParserError
        items = soup.find_all('item')
        feed = soup.find('title').get_text(strip=True)
        news_on_page = self._get_tag_content(items)
        news = {'Feed': feed,
                'items': news_on_page}
        return news

    def _get_tag_content(self, items: bs4.element.ResultSet) -> List[dict]:
        """
        Get content for each tag plus find image
        :param items: element of items
        :return:
        """
        self.logger.info('Processing tags')
        all_news = []
        tags = ['title', 'link', 'pubDate', 'description']
        for item in items:
            current_news = {}
            for tag in tags:
                for tag_content in item.contents:
                    if tag == tag_content.name:
                        if tag_content.name == 'description':
                            current_news[tag] = bs4.BeautifulSoup(tag_content.text, 'lxml').get_text(strip=True)
                        elif tag_content.name == 'pubDate':
                            current_news[tag] = self._date_converter(tag_content.text)
                        else:
                            current_news[tag] = tag_content.text
            current_news['image'] = self.find_image(item)
            all_news.append(current_news)
        self.logger.info('Processing tags is done')
        return all_news

    @staticmethod
    def _date_converter(date: str) -> datetime.strftime or None:
        """
        Convert to human readable format
        :param date: Input date
        :return:
        """
        keys = ["%a, %d %b %Y %H:%M:%S %z",
                '%Y-%m-%dT%H:%M:%SZ',
                "%a, %d %b %Y %H:%M:%S %Z"
                ]
        for key in keys:
            try:
                date_obj = datetime.strptime(date, key)
            except ValueError:
                date_obj = None
            if isinstance(date_obj, datetime):
                return date_obj.strftime("%a, %d %b %Y %H:%M:%S")

    def _arg_date_check(self):
        """
        Convert self.date to datetime objecte
        and check correctly input date in command line
        :return:
        """
        try:
            date_obj = datetime.strptime(self.date, '%Y%m%d')
            return date_obj.strftime("%a, %d %b %Y %H:%M:%S")[:-9]
        except ValueError as er:
            print(er, 'Please entered correct date', sep='\n')

    def read_json(self) -> Optional[dict]:
        """Read json file
        :return: dict from json file

        """
        try:
            self.logger.info(f"Start read in file: {self.json_link}")
            with open(self.json_link, 'r') as file:
                self.logger.info("End read json file!")
                return json.load(file)
        except FileNotFoundError:
            print("File is not found, cant read data-cache. "
                  "It is necessary to save any data")
            raise ParserError

    def write_json(self):
        """
        Write result in json file
        :return: None
        """
        self.logger.info(f"Start writing in file: {self.json_link}")
        with open(self.json_link, 'w') as file:
            json.dump(self.items_dict, file, indent=2, ensure_ascii=False)
            self.logger.info("End writing in file: {}".format(self.json_link))

    @staticmethod
    def find_image(item: bs4.element.ResultSet) -> Optional[List[str] or str]:
        """
        Find all images(png, jpg, jpeg) for this item
        :param item: element of items
        :return: url of image or none
        """
        url_pattern = re.compile(r'https?://[a-zA-Z0-9_\-/~\.:]+')

        try:
            image_links = []
            all_links = re.findall(url_pattern, item.text)
            for link in all_links:
                image_links.append(link) if re.search(f'(jpeg|png|jpg)', link) else None
            return image_links[0] if len(image_links) > 0 else 'Images not found'
        except NameError:
            print('Image error def')

    @staticmethod
    def _format(news_item: dict) -> str:
        """Convert dict on output str
        :param news_item: element of rss object
        :return: str
        """
        output_keys = ['title', 'pubDate', 'link', 'description']
        output_links = ['link', 'image']
        output_string = ''
        for key in output_keys:
            content = news_item.get(key)
            if content is not None:
                output_string += key.capitalize() + ': ' + news_item.get(key) + '\n'
        output_string += '\n\nlinks:\n'
        for link in output_links:
            content = news_item.get(link)
            if content is not None:
                output_string += link.capitalize() + ': ' + news_item.get(link) + '\n'
        output_string += "\n"
        return output_string

    def output_title_page(self) -> str:
        """
        Print in stdout content(news) if url not exist
        :return:
        """
        return self.items_dict['Feed']

    def output_format(self) -> str:
        """
        Print in stdout content(news) if self.url exist
        :return:
        """
        if self.json_format:
            self.logger.info("Convert object in str(json) for __str__")
            output = ""
            counter = 0
            for news in self:
                if not news["pubDate"] and self.date or self.date and self.date \
                        not in news["pubDate"]:
                    continue
                elif counter == self.limit:
                    break
                else:
                    output += json.dumps(news, indent=2, ensure_ascii=False)
                    counter += 1
        else:
            self.logger.info("Convert object in str for __str__")
            output = "Feed: " + self.items_dict["Feed"] + "\n"
            counter = 0
            for news in self:
                if not news["pubDate"] and self.date or self.date and self.date \
                        not in news["pubDate"]:
                    continue
                elif counter == self.limit:
                    break
                else:
                    counter += 1
                    output += self._format(news)
        return output

    def __getitem__(self, item):
        return self.items_dict["items"][item]

    def __str__(self) -> str:
        return self.output_format()
