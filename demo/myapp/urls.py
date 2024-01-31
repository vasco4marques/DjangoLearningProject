from django.urls import path
from . import views
from register import views as regView

urlpatterns = [
    path("", views.home, name="home"), # When we go to "" path, we go to the home view
    path("todos/", views.todolists, name = "To Do Lists"), # Se for para o /todos vai para a página views.todos
    path("Create-new-list/",views.newList, name = "newList"),
    path("Delete-a-list/", views.removeList, name = "DeleteList"),
    path("todos/<str:name>" , views.todos ,name="List"),
    path("register/", regView.register, name="Register"),
   
]