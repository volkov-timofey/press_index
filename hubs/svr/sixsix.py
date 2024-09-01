from urllib.parse import urljoin
from datetime import datetime

import chardet

from config import HEADERS
from connect.article import get_title, get_published_date, get_url, get_author_information
from connect.main_news_page import NewsParser


class SixSix(NewsParser):
    def __init__(self, url_hub: str, name, soup_attrs: dict = {}):
        super().__init__(url_hub, name, soup_attrs)

    def _clean__url_pages(self):
        row_url_pages = self.extract_articles()
        return [url_ for url_ in row_url_pages if 'news' in url_]

    def get_author_information(self, soup) -> dict|None:
        """
        Get authors article
        :param soup:
        :return:
        """
        author_object = soup.find('div', {'class': 'news-piece-layout__caption-author'})
        if author_object:
            author_name = author_object.get_text()
            author_url = urljoin(
                self.url_hub,
                author_object.find('a', href=True).get('href')
            )
            print(f'Автор: {author_name}, url: {author_url}')
            return {
                'authors_full_name': author_name,
                'author_url': author_url
            }
        print(f'Автор: не обнаружен')

    @staticmethod
    def get_text_article(soup):
        """
        Get text articles with 'itemprop' = 'articleBody'
        :param soup:
        :return:
        """
        text_object = soup.find('div', {'itemprop': 'articleBody'})
        text_article = '/n'.join([p.get_text() for p in text_object.find_all('p')]) \
            if text_object \
            else text_object

        print(f'Статья: {text_article or "Содержание не обнаружено"}')
        return text_article

    def get_information(self, sub_url):
        url_ = urljoin(self.url_hub, sub_url)
        soup = self.get_html_page(url_, {}, HEADERS)

        article_information = {
            'title': get_title(soup),
            'date_published': get_published_date(soup),
            'url': get_url(soup)
        }

        author_information = self.get_author_information(soup)
        if author_information:
            article_information = {
                **article_information,
                **author_information
            }

        article_information['text_article'] = self.get_text_article(soup)
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

if __name__ == "__main__":
    url = "https://www.66.ru"
    name = 'a'
    attrs = {"class": "new-news-piece__link"}
    ria = SixSix(url, name, attrs)
    ria.get_result()