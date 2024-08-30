import requests
from bs4 import BeautifulSoup
import time
import datetime
from typing import List, Dict, Any
import json
import re


# Headers для запроса
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ru;q=0.8,af;q=0.7"
}

# Ключевые слова (взял рандомные слова)
keywords = []


class HttpResponse:
    def get_response(self, url, params=None, headers=None):
        """
        Выполняем запрос по ссылке
        """
        response = requests.request(
            method="GET",
            url=url,
            params=params,
            headers=headers
        )
        return self.check_response(response)

    def check_response(self, response: requests.Response):
        """
        Проверка статуса запроса
        """
        if response.status_code == 200:
            return response
        else:
            error_message = f"Your request returned {response.status_code} status code."
            if response.status_code == 404:
                error_message += " The requested resource wasn't found."
            elif response.status_code == 500:
                error_message += " The server encountered an internal error."
            raise Exception(error_message)


class NewsParser:
    def __init__(self):
        self.http_response = HttpResponse()

    def get_html_page(self,
                      article_url: str,
                      params: Dict[str, Any] = None,
                      headers: Dict[str, Any] = None
                      ) -> BeautifulSoup:
        """
        Получение HTML кода страницы
        """
        response = self.http_response.get_response(article_url, params, headers)
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup)
        return soup

    def get_pages(self, soup: BeautifulSoup) -> List[str]:
        """
        Возвращаем список страниц с новостями
        """
        pages = []
        # interfax.ru links = soup.find_all("a", {"tabindex": "5"})
        # 66.ru links = soup.find_all("a", {"class": "new-news-piece__link"})
        for href in links:
            pages.append(href.get("href"))
        return pages


    def return_info(self, url, params, headers):
        """
        Возврат новостей в списке и в JSON файле
        """
        soup = self.get_html_page(article_url=url, params=params, headers=headers)
        pages = self.get_pages(soup)

        return pages

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


    def main(self):
        """
        Основной блок программы
        """
        # Основная ссылка (ТОЛЬКО ГЛАВНЫЕ СТРАНИЦЫ САЙТОВ)
        url = f"https://www.interfax.ru"
        # https://aif.ru попробовать
        # https://www.kommersant.ru (можно рассмотреть)
        # https://iz.ru !!! номер 1, остальные по накатке!!!
        # https://www.interfax.ru
        # 66.ru
        # https://russian.rt.com
        # https://rg.ru внизу страницы есть json для выкачивания
        # https://vz.ru (есть разметка)

        # params запроса
        params = {}

        news = self.return_info(url=url, params=params, headers=HEADERS)
        print(news)


if __name__ == "__main__":
    ria = NewsParser()
    ria.main()
