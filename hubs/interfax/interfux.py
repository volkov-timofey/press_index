from urllib.parse import urljoin
from datetime import datetime, date

from connect.article import get_title, get_published_date, get_url
from connect.main_news_page import NewsParser


class Interfux(NewsParser):
    """
    Model parser for Interfux
    """
    def __init__(self):
        url_hub = "https://www.interfax.ru"
        soup_attrs = {"tabindex": "5"}
        super().__init__(url_hub, soup_attrs)

    def _clean__url_pages(self) -> list:
        """
        Custom clean urls
        :return:
        """
        row_url_pages = self.extract_articles()
        return [url_ for url_ in row_url_pages if 'https' not in url_]

    @staticmethod
    def get_published_date(soup) -> date:
        """
        Get published date
        :param soup:
        :return:
        """
        published_time = soup.find('meta', property="article:published_time")

        if not published_time:
            print("Время публикации: отсутствует")
            return published_time

        published_time = published_time.get('content')
        published_date = datetime.strptime(
            published_time, '%Y-%m-%dT%H:%M%z'
        ).date()

        print("Время публикации:", published_date)
        return published_date

    @staticmethod
    def get_text_article(soup) -> str|None:
        """
        Get text articles with 'itemprop' = 'articleBody'
        :param soup:
        :return:
        """
        text_object = soup.find('article', {'itemprop': 'articleBody'})

        text_article = '/n'.join(
            [p.get_text() for p in text_object.find_all('p')]
        ) if text_object else text_object

        print(f'Статья: {text_article or "Содержание не обнаружено"}')
        return text_article

    def get_information(self, sub_url: str) -> dict:
        """
        Get full information about article
        :param sub_url: str
        :return: dict
        """
        url_ = urljoin(self.url_hub, sub_url)
        soup = self.get_html_page(url_)

        article_information = {
            'title': get_title(soup),
            'date_published': self.get_published_date(soup),
            'url': get_url(soup),
            'article': self.get_text_article(soup)
        }

        return article_information

    def get_result(self):
        """
        Generator articles
        :return:
        """
        return (
            self.get_information(page)
            for page in self._clean__url_pages()
        )
