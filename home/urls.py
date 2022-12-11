from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("track/", views.track, name="track"),
    path("search/", views.search, name="search"),
]
