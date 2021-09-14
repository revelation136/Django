from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    # adding the dynamic response on path
    path("<str:name>", views.greet, name='greet'),
    ]
