import pytest

from Artem_Kasperovich.project.parse_news import ParserError


@pytest.mark.parametrize('correct_link', ('https://people.onliner.by/feed',
                                          'https://www.thecipherbrief.com',
                                          'https://news.yahoo.com/'))
def test_check_correct_link_processed(parser, correct_link):
    assert parser.get_response(correct_link).ok


@pytest.mark.parametrize('incorrect_link', ('https://people.onlkkkkkiner.y/feedlllllll',
                                            22222,
                                            [],
                                            ''))
def test_check_incorrect_link_processed(parser, incorrect_link):
    with pytest.raises(ParserError):
        parser.get_response(incorrect_link)


@pytest.mark.parametrize('correct_link', ('https://people.onliner.by/feed',
                                          'https://www.thecipherbrief.com/feed',
                                          'https://news.yahoo.com/rss/'))
def test_check_successful_parsed(parser, correct_link):
    response = parser.get_response(correct_link)
    parsing_result = parser.parsing_rss(response)
    assert parsing_result


@pytest.mark.parametrize('not_rss_link', ('https://stackoverflow.com/',
                                          'https://www.onliner.by/',
                                          'https://www.youtube.com/'))
def test_check_not_rss_link(parser, not_rss_link):
    response = parser.get_response(not_rss_link)
    with pytest.raises(ParserError):
        parser.parsing_rss(response)


def test_check_readable_ability(parser):
    result = parser.read_json()
    assert result
