from django.urls import path

from .views import MovieDetailView, MovieView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDetailView.as_view()),
]
