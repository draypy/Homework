from pytest import fixture, mark
from Artem_Kasperovich.project.parse_news import NewsParser


@fixture(scope='function')
def parser():
    return NewsParser()

