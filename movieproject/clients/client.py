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
# print(check_new_url)
# print(check_new_url['poster_path'])
# print(check_new_url['title'])


top_rated_urls = "https://api.themoviedb.org/3/movie/top_rated/?api_key=3a52b2ae849a177b7117edd478a2e3e9&language=en-US"


def get_top_movies(top_rated_urls):
    response = requests.get(top_rated_urls)
    data = response.json()
    return data['results']


top_rated_movies = get_top_movies(top_rated_urls)
# print(type(top_rated_movies))
# print(top_rated_movies)

for resul in top_rated_movies:
    print(resul['title'])
    print(resul['poster_path'])
    print(resul['vote_average'])
    print(resul['id'])
