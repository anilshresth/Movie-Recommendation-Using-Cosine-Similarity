import requests


base_url = 'https://api.themoviedb.org/3/movie/upcoming/?api_key=3a52b2ae849a177b7117edd478a2e3e9&language=en-US'


def get_upcoming_movies(base_url):
    response = requests.get(base_url)
    data = response.json()
    return data['results'], data['dates']


upcoming_movies, upcoming_dates = get_upcoming_movies(base_url)
print(upcoming_dates)
count = 0
for resul in upcoming_movies:

    if count < 5:
        print(resul['title'])
        print(resul['poster_path'])
        print(resul['id'])
        count += 1
