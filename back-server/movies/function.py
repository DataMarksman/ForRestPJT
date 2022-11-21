import requests
import json
import os
# from .serializers import *
# from .models import *

# TMDB_API_KEY = "f555794485796214438961ced766522e"

# def get_movie_datas():
#     total_data = []

#     for i in range(1, 2):
#         request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
#         movies = requests.get(request_url).json()

#         for movie in movies['results']:
#             if movie.get('release_date', ''):
#                 fields = {
#                     'movie_id': movie['id'],
#                     'title': movie['title'],
#                     'released_date': movie['release_date'],
#                     'popularity': movie['popularity'],
#                     'overview': movie['overview'],
#                     'poster_path': movie['poster_path'],
#                 }

#                 data = {
#                     "pk": movie['id'],
#                     "model": "movies.movie",
#                     "fields": fields
#                 }

#                 total_data.append(data)

#     with open("movie_data.json", "w", encoding="utf-8") as w:
#         json.dump(total_data, w, indent="", ensure_ascii=False)

# get_movie_datas()

TMDB_API_KEY = "f555794485796214438961ced766522e"

BASIC_URL = "https://image.tmdb.org/t/p/w500/"

def get_movie_datas():
    total_data = []

    for i in range(1, 11):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'tmdb_id': movie['id'],
                    'title': movie['title'],
                    'original_title': movie['original_title'],
                    'release_date': movie['release_date'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'popularity': movie['popularity'],
                    'poster_path': BASIC_URL+movie['poster_path'],
                    'adult': movie['adult']
                }
                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)
                # serializer = MovieSerializer(data=data)
                # if serializer.is_valid(raise_exception=True):
                #     serializer.save()

    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="", ensure_ascii=False)

get_movie_datas()
