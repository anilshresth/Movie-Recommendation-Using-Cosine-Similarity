import enum
import os


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests


def recommendations(movie_title):
    movie_lists = []
    poster_lists = []
    movie_overviews = []

    work_path = os.path.dirname(os.path.abspath(__file__))

    df = pd.read_csv(os.path.join(
        work_path, 'movie_dataset.csv'), low_memory=False)

    # replace all the empty values with a empty string
    features = ['keywords', 'cast', 'genres', 'director']

    for feature in features:
        df[feature] = df[feature].fillna('')

    def combine_relevant_columns(row):
        return row["keywords"] + " " + row['cast']+row['genres']+row['director']

    df['combined_features'] = df.apply(combine_relevant_columns, axis=1)

    # feature extraction using sklearn
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])
    print("Count Matrix:", count_matrix.toarray())

    cosine_sim = cosine_similarity(count_matrix)

    movie_user_likes = movie_title

    def get_index_from_title(title):
        return df[df.title == title]["index"].values[0]

    movie_index = get_index_from_title(movie_user_likes)

    similar_movies = list(enumerate(cosine_sim[movie_index]))

    def get_title_from_index(index):
        return df[df.index == index]["title"].values[0]

    sorted_similar_movies = sorted(
        similar_movies, key=lambda x: x[1], reverse=True)

    def get_movie_indexid(id):
        return df[df['index'] == id]['id'].values[0]

    def get_poster_path(movie_id):
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=3a52b2ae849a177b7117edd478a2e3e9&language=en-US'
        response = requests.get(url)
        data = response.json()
        return data['poster_path'], data['overview']

    for counter, movie in enumerate(sorted_similar_movies):
        if counter < 5:
            movie_lists.append(get_title_from_index(movie[0]))
            movie_id = get_movie_indexid(movie[0])
            poster_path, overview = get_poster_path(movie_id)
            poster_lists.append(poster_path)
            movie_overviews.append(overview)

        else:
            break

    return movie_lists, poster_lists, movie_overviews
