from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), #When we go to "" path, we go to the home view
    path("todos/", views.todos, name = "Todos")
]