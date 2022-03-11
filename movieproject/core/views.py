from django.shortcuts import render
import time
import pandas as pd
import os
from django.http import HttpResponse
import requests

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .recommedations import recommendations

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

    df["image_urls"] = df['id'][:6].map(
        get_image_url_path)

    for index, row in df.iterrows():
        if index <= 5:
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
            'movie_zipped': movie_zipped

        }
        return render(request, 'core/movie_detail.html', context=context)

    return HttpResponse("details to the movie not found")
