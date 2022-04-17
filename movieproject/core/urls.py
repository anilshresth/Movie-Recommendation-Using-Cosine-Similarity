from turtle import home
from django.urls import path
from .views import homepage, movie_detail,moviewatchlist

urlpatterns = [
    path("", homepage, name="movie_list"),
    path('movie_detail/<int:id>/',
         movie_detail, name="movie_detail"),
    path('movie-watchlist/',moviewatchlist,name='moviewatchlist')

]
