from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), # When we go to "" path, we go to the home view
    path("todos/", views.todolists, name = "To Do Lists"), # Se for para o /todos vai para a página views.todos
    path("todos/<str:name>" , views.todos ,name="List")
]