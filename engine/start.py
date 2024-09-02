import os
import aiohttp
import asyncio

from db.database import DataBase
from dotenv import load_dotenv

from hubs.interfax.interfux import Interfux
from hubs.rt.rt import RT
from hubs.svr.sixsix import SixSix


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
MAPPING_HUBS = {
    'https://www.interfax.ru': {
        'model': Interfux(),
        'fields_article': (
            'hub_id', 'title', 'date_published', 'url', 'article'
        )
    },
    'https://www.66.ru': {
        'model': SixSix(),
        'fields_article': ('hub_id', 'title', 'date_published',
                           'url', 'article', 'author_full_name', 'author_url')
    },
    'https://russian.rt.com': {
        'model': RT(),
        'fields_article': ('hub_id', 'title', 'date_published',
                           'url', 'article', 'author_full_name')
    }
}


async def insert_data_to_db(data_hub: tuple):
    """
    Insert articles for hub
    :param data_hub:
    :return:
    """
    db = DataBase(DATABASE_URL)

    id_, _, url_hub, interval, _ = data_hub

    config_hub = MAPPING_HUBS[url_hub]
    model_hub = config_hub.get('model')
    gen_result = model_hub.get_result()
    name_table = 'articles'

    fields_article = config_hub.get('fields_article')

    for page in gen_result:
        values = [id_]
        values.extend([page.get(field) for field in fields_article[1:]])
        if not db.get_data_table(name_table, 'url', ('url', page.get('url'))):
            db.change_table(name_table, fields_article, tuple(values))

    await asyncio.sleep(interval)


async def main():
    while True:
        db = DataBase(DATABASE_URL)

        list_hubs = db.get_data_table('hubs_hub')
        tasks = [insert_data_to_db(data_hub) for data_hub in list_hubs]

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())

