from pydoc import resolve
import requests
import json
import logging


api_key = "3a52b2ae849a177b7117edd478a2e3e9"
url = 'https://api.themoviedb.org/3/find/tt0114709?api_key=3a52b2ae849a177b7117edd478a2e3e9&external_source=imdb_id'


def get_image_url(url):
    resp = requests.get(url)
    data = resp.json()
    movies_detail = data['movie_results']

    return movies_detail[0]['poster_path'], movies_detail[0]['title']


# response = requests.get(url)
# print(response.status_code)
# data = response.json()
# movies_detail = data['movie_results']


# print(type(movies_detail))
# print(movies_detail[0]['poster_path'])
# path, title = get_image_url(url)
# print(path)
# print(title)
base_url = "https://api.themoviedb.org/3/movie/862?api_key=3a52b2ae849a177b7117edd478a2e3e9&language=en-US"


def get_image_url_path(base_url):
    response = requests.get(base_url)
    data = response.json()
    return data


check_new_url = get_image_url_path(base_url=base_url)
print(check_new_url['poster_path'])
print(check_new_url['title'])
