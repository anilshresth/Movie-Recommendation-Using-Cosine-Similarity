from django.shortcuts import render
import time
import pandas as pd
import os
from django.http import HttpResponse
import requests

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .recommedations import recommendations
from users.models import Movie

# Create your views here.
work_path = os.path.dirname(os.path.abspath(__file__))
dir_base = os.getcwd()
image_url = 'https://image.tmdb.org/t/p/w500'


def homepage(request):
    csv_rows = []

    df = pd.read_csv(os.path.join(
        work_path, 'movie_dataset.csv'), low_memory=False)

    def get_image_url_path(id):
        base_url = f"https://api.themoviedb.org/3/movie/{id}?api_key=3a52b2ae849a177b7117edd478a2e3e9&language=en-US"
        response = requests.get(base_url)
        time.sleep(0.5)
        data = response.json()
        return data['poster_path']

    df["image_urls"] = df['id'][:20].map(
        get_image_url_path)

    for index, row in df.iterrows():
        if index < 20:
            csv_rows.append(row)

        else:
            break

    context = {
        'data': csv_rows
    }
    return render(request, template_name="core/movie_list.html", context=context)


def movie_detail(request, id):
    image_url = None
    csv_detail = []
    image_urls = ''
    df = pd.read_csv(os.path.join(
        work_path, 'movie_dataset.csv'),  low_memory=False)
    movie_detail = df[df['id'] == id]
    print(movie_detail)

    genres = list(movie_detail['genres'])

    def get_image_url(id):
        base_url = f"https://api.themoviedb.org/3/movie/{id}?api_key=3a52b2ae849a177b7117edd478a2e3e9&language=en-US"
        response = requests.get(base_url)
        time.sleep(0.5)
        data = response.json()
        return data['poster_path'], data['title']

    image_url, title = get_image_url(id)

    image_urls = image_url

    if len(movie_detail) > 0:
        for index, row in movie_detail.iterrows():
            csv_detail.append(row)
        movie_names, poster_paths, movie_overviews = recommendations(title)
        movie_zipped = zip(movie_names, poster_paths, movie_overviews)

        context = {
            'csv_detail': csv_detail,
            'image_urls': image_urls,
            'genres': genres,
            'movie_zipped': movie_zipped


        }
        return render(request, 'core/movie_detail.html', context=context)

    return HttpResponse("details to the movie not found")


def moviewatchlist(request):
    movie_watch_list = Movie.objects.filter(user=request.user)
    image_urls = list()
    movie_titles = list()
    movies_homepages = list()

    def get_image_url_path(id):
        base_url = f"https://api.themoviedb.org/3/movie/{id}?api_key=3a52b2ae849a177b7117edd478a2e3e9&language=en-US"
        response = requests.get(base_url)
        time.sleep(0.5)
        data = response.json()
        return data['poster_path'], data['title'], data['homepage']

    for movie in movie_watch_list:
        print(movie.id)
        image_url, movie_title, movie_homepage = get_image_url_path(
            movie.movie_id)
        image_urls.append(image_url)
        movie_titles.append(movie_title)
        movies_homepages.append(movie_homepage)

    movie_zipped = zip(image_urls, movie_titles, movies_homepages)
    # print(image_urls)
    context = {
        'movie_zipped': movie_zipped
    }

    if movie_watch_list:
        return render(request, 'core/personal_movie_list.html', context=context)
    else:
        return HttpResponse('no object found for the user')
