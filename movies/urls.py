from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #Mantener id 
    path("movie/<int:movie_id>/", views.movie, name="movie_id"),
]




