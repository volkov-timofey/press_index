from datetime import datetime, date


def get_title(soup) -> str:
    """
    Get title article
    :param soup:
    :return:
    """
    og_title = soup.find('meta', property='og:title')
    og_title = og_title.get('content')
    print("Заголовок страницы:", og_title)
    return og_title

def get_url(soup) -> str:
    """
    Get url article
    :param soup:
    :return:
    """
    og_url = soup.find('meta', property='og:url')
    og_url = og_url.get('content')
    print("URL:", og_url)
    return og_url

def get_published_date(soup) -> date:
    """
    Get published date
    :param soup:
    :return:
    """
    published_time = soup.find('meta', {'name': 'mediator_published_time'})
    if not published_time:
        print("Время публикации: отсутствует")
        return published_time
    published_time = published_time.get('content')
    published_date = datetime.strptime(published_time, '%Y-%m-%dT%H:%M:%S%z').date()
    print("Время публикации:", published_date)
    return published_date


def get_author_information(soup) -> list | None:
    """
    Get authors article
    :param soup:
    :return:
    """
    author_object = soup.find_all('meta', {'name': 'mediator_author'})
    if not author_object:
        print(f'Автор не найден')
        return author_object

    authors = [autor.get('content') for autor in author_object]
    names = ', '.join(authors)
    print(f'Автор: {names}')
    return authors
