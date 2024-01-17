from django.shortcuts import render, HttpResponse
from .models import ToDoList, Item
# Create your views here.

def home(request):
    return render(request, "home.html")

def todolists(request):
    lista = ToDoList.objects.all()
    return render(request, "todos.html", {"listas":lista})

def todos(request, name):
    newName = name.replace("%20"," ")
    lista= ToDoList.objects.get(name=newName)
    todos = lista.item_set.all()
    return render(request, "todos-full-list.html", {"name": newName, "todos": todos} )