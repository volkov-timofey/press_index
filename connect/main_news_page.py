from typing import Dict, Any, List

from bs4 import BeautifulSoup

from connect.check_connection import HttpResponse
from config import HEADERS


class NewsParser:
    def __init__(self, soup_attrs: dict, url_hub: str):
        self.http_response = HttpResponse()
        self.soup_attrs = soup_attrs
        self.url_hub = url_hub

    def get_html_page(
            self,
            article_url: str,
            params: Dict[str, Any] = None,
            headers: Dict[str, Any] = None
    ) -> BeautifulSoup:
        """
        Получение HTML кода страницы
        """
        response = self.http_response.get_response(article_url, params, headers)
        soup = BeautifulSoup(response.text, "html.parser")
        #print(soup)
        return soup

    def get_pages(self, soup: BeautifulSoup) -> List[str]:
        """
        Возвращаем список страниц с новостями
        """
        links = soup.find_all("a", self.soup_attrs) #interfax.ru
        # 66.ru links = soup.find_all("a", {"class": "new-news-piece__link"})
        pages = [href.get("href") for href in links]
        return pages


    def extract_articles(self, url, params, headers):
        """
        Возврат новостей
        """
        soup = self.get_html_page(article_url=url, params=params, headers=headers)
        pages = self.get_pages(soup)

        return pages


    def main(self):
        """
        Основной блок программы
        """
        # params запроса
        params = {}

        news = self.extract_articles(url=url, params=params, headers=HEADERS)
        print(news)

if __name__ == "__main__":
    url = f"https://www.interfax.ru"
    attrs = {"tabindex": "5"}
    ria = NewsParser(attrs, url)
    ria.main()



def extract_from_article(self):
    # 66.ru
    ''
    '<h1 class="text__h1">Бывший вице-президент «Города без наркотиков» уехал на спецоперацию</h1>'
    """
    <div class="news-piece-layout__caption-date">Сегодня, 16:33</div>
    <div class="news-piece-layout__caption-author"><a href="/news/editor/47/">Дмитрий Антоненков</a></div>
    """
    # interfax
    """
    <meta property="og:url" content="https://www.interfax.ru/russia/978898" />
    <meta property="og:description" content="В министерстве обороны РФ сообщили, что бомбардировщик Су-34 ВКС России нанес удар по живой силе и бронетехнике ВСУ в приграничном районе Курской области." />
    <meta property="og:site_name" content="Interfax.ru" />
    <meta property="og:locale" content="ru_RU" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="Бомбардировщик Су-34 нанес удар по позициям ВСУ в Курской области"/>
    <meta property="og:image" content="https://www.interfax.ru/aspimg/978898.png" />
    <meta property="article:section" content="В России"/>
    <meta property="article:published_time" content="2024-08-30T16:04+0300"/>
    <meta property="twitter:title" content="Бомбардировщик Су-34 нанес удар по позициям ВСУ в Курской области"/>
    <meta property="twitter:description" content="В министерстве обороны РФ сообщили, что бомбардировщик Су-34 ВКС России нанес удар по живой силе и бронетехнике ВСУ в приграничном районе Курской области." />
    <meta property="twitter:site" content="@interfax_news" />
    <meta property="twitter:url" content="https://www.interfax.ru/russia/978898" />
    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:image" content="https://www.interfax.ru/aspimg/978898.png" />
    <meta property="article:tag" content="Минобороны РФ"/>
    <meta property="article:tag" content="Курская область"/>
    """

# Основная ссылка (ТОЛЬКО ГЛАВНЫЕ СТРАНИЦЫ САЙТОВ)

# https://aif.ru попробовать
# https://www.kommersant.ru (можно рассмотреть)
# https://iz.ru !!! номер 1, остальные по накатке!!!
# https://www.interfax.ru
# 66.ru
# https://russian.rt.com
# https://rg.ru внизу страницы есть json для выкачивания
# https://vz.ru (есть разметка)