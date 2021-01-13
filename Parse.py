import requests
from bs4 import BeautifulSoup
import json
import logging

logging.basicConfig(level=logging.DEBUG, filename='debug.log', format='[%(asctime)s] %(levelname)s:%(message)s')
filters = {
    'title_type': 'feature',
    'release_date-min': '2000-02-01',
    'release_date-max': '2010-01-01',
    'genres': [],
    'user_rating-min': '5.5',
    'user_rating-max': '10',
    'countries': ['dk'],
    'count': '250',
}
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru-RU,ru;q=0.9",
    "content-type": "application/x-www-form-urlencoded"
}
imdb_page = 'https://www.imdb.com'


def parsing():
    souops = []
    mass_numbers = ['1', '251', '501', '751']
    all_films_dict = {}
    for number in mass_numbers:
        filters['start'] = number
        page = requests.post(imdb_page + '/search/title/', headers=headers, params=filters)
        abc = BeautifulSoup(page.text, 'html.parser')
        number_soups = abc.find('div', class_='desc')
        souops.append(abc)
        if number_soups.text.split()[-1] == 'Previous':
            break
    for soup in souops:
        films = soup.findAll('div', class_="lister-item-image float-left")

        for film in films:
            try:
                dict_movie = {}

                name = film.img.get('alt')
                link = film.a.get('href')

                film_html = requests.post(imdb_page + link, headers=headers)
                film_soup = BeautifulSoup(film_html.text, 'html.parser')
                json_soup = film_soup.find("script", type="application/ld+json")
                json_film_info = json.loads(json_soup.string)

                try:
                    dict_movie['Title'] = name
                except:
                    pass
                try:
                    dict_movie['Genres'] = json_film_info['genre']
                except:
                    pass
                try:
                    dict_movie['Rating'] = json_film_info['aggregateRating']['ratingValue']
                except:
                    pass
                try:
                    actors = []
                    for actor in json_film_info['actor']:
                        actors.append(actor['name'])
                    dict_movie['TopActors'] = actors
                except:
                    pass
                try:
                    dict_movie['Type'] = json_film_info['@type']
                except:
                    pass
                films_details = film_soup.select('div#titleDetails div.txt-block')
                det = [tag.text for tag in films_details]
                details = ''
                for i in det:
                    details += i.replace('\n', '\xa0'). \
                        replace('IMDbPro\xa0»', ''). \
                        replace('See more\xa0»', ''). \
                        replace('Show more on', ''). \
                        replace('See full technical specs\xa0»', ''). \
                        replace('Edit', ''). \
                        replace('Details', ''). \
                        replace('|', ',')
                dict_movie['Details'] = details
                all_films_dict[name] = dict_movie
            except Exception as exception:
                logging.error(f'Parsing failed {exception}')
                return exception

    return all_films_dict


if __name__ == '__main__':
    result = parsing()
    try:
        with open('films_list.json', 'w', encoding='utf-8') as Json:
            json.dump(result, Json, ensure_ascii=False)
            logging.info('Json file is created')

    except Exception as exception:
        logging.error(f'Json file is failed to create {exception}')
