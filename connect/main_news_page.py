from bs4 import BeautifulSoup

from connect.check_connection import HttpResponse


class NewsParser(HttpResponse):
    def __init__(self, url_hub: str, soup_attrs):
        self.url_hub = url_hub
        self.soup_attrs = soup_attrs

    def get_html_page(
            self,
            url_hub: str
    ) -> BeautifulSoup:
        """
        Get html code page
        """
        response = self.get_response(url_hub)
        soup_main_page = BeautifulSoup(response.text, "html.parser")

        return soup_main_page

    def get_pages(self, soup: BeautifulSoup) -> list:
        """
        Get list pages with news
        """
        links = soup.find_all('a', self.soup_attrs)

        return [href.get("href") for href in links]


    def extract_articles(self):
        """
        Get articles page
        """
        soup_main_page = self.get_html_page(url_hub=self.url_hub)
        pages_article = self.get_pages(soup_main_page)

        return pages_article
