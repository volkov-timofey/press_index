from urllib.parse import urljoin
from datetime import datetime

from bs4 import BeautifulSoup

from connect.article import get_title, get_published_date, get_url, get_author_information
from connect.main_news_page import NewsParser


class RT(NewsParser):
    """
    Model parser for Russia Today
    """
    def __init__(self):
        url_hub = "https://russian.rt.com"
        soup_attrs = {"class": "link link_color"}
        super().__init__(url_hub, soup_attrs)

    def _clean__url_pages(self) -> list:
        """
        Custom clean urls
        :return:
        """
        row_url_pages = self.extract_articles()
        return [
            url_ for url_ in row_url_pages
            if 'article' in url_ or 'news' in url_
        ]

    @staticmethod
    def get_text_article(soup) -> str|None:
        """
        Get text articles with class article__text
        :param soup:
        :return:
        """
        text_object = soup.find('div', {'class': 'article__text'})
        text_article = '/n'.join([p.get_text() for p in text_object.find_all('p')])\
            if text_object\
            else text_object

        print(f'Статья: {text_article or "Текст не обнаружен"}')
        return text_article

    def get_information(self, sub_url: str) -> dict:
        """
        Get full information about article
        :param sub_url:
        :return:
        """
        url_ = urljoin(self.url_hub, sub_url)
        soup = self.get_html_page(url_)

        return {
            'title': get_title(soup),
            'date_published': get_published_date(soup),
            'url': get_url(soup),
            'author_full_name': get_author_information(soup),
            'article': self.get_text_article(soup)
        }

    def get_result(self):
        """
        Generator articles
        :return:
        """
        return (
            self.get_information(page)
            for page in self._clean__url_pages()
        )
