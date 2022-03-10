import requests


def get_poster_path(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3a52b2ae849a177b7117edd478a2e3e9&language=en-US"
    response = requests.get(url)
    data = response.json()
    return data


data = get_poster_path(207)
print(data)

print(data['poster_path'])
print(data['overview'])
