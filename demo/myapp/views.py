from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList,deleteList

# Create your views here.

# O dicionário leva  {"nome_variavel" : valor}
# Nos files html é como se tivessemos nome_variavel = valor

def home(request):
    return render(request, "home.html",{})

def todolists(request):
    return render(request, "lists.html")


def saveAll(request,name):
    newName = name.replace("%20"," ")
    user = request.user
    todos = ToDoList.objects.get(user=user).item_set.all()

    for item in todos:
        if request.POST.get("c"+str(item.id)) == "clicked":
            item.complete = True
        else:
            item.complete=False
        item.save()

def todos(request, name):   
    newName = name.replace("%20"," ")
    lista= ToDoList.objects.get(name=newName)
    todos = lista.item_set.all()

    print(request.POST)
    if request.method == "POST":
        
        # If button "Save" is pressed
        if request.POST.get("save"):
            saveAll(request,name)
            return HttpResponseRedirect(f"/todos/{name}")
        
        # If "Add Item" is clicked 
        elif request.POST.get("newItem"):
            txt = request.POST.get("new")
            if len(txt) > 2:
                lista.item_set.create(text=txt,complete = False)
            else:
                print("invalid")

            return HttpResponseRedirect(f"/todos/{name}")
        
        # If "Remove Finished" button is clicked (automaticaly saves)
        elif request.POST.get("remove"):
            t = []
            saveAll(request,name)
            for item in todos:
                if item.complete:
                    t.append(item)
            
            for toRemove in t:
                lista.item_set.get(id=toRemove.id).delete() 
            
            return HttpResponseRedirect(f"/todos/{name}")

    return render(request, "todos.html", {"name": newName, "todos": todos} )


def newList(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            lista = ToDoList.objects.all()
            var = False
            for item in lista:
                if item.name == n:
                    var = True
            if var:
                return HttpResponse("<h1>Não podem haver 2 listas com o mesmo nome <a href = '/todyos'>Back to Listas</a></h1>")          
            
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)
            return HttpResponseRedirect('/todos')    
    else:
        form = CreateNewList()
    return render(request, "newList.html" ,{"form":form})

def removeList(request):
    form = deleteList(request.GET)
    if form.is_valid():
        name = form.cleaned_data["name"]
        lista = ToDoList.objects.get(name = name)
        lista.delete()
        return HttpResponseRedirect('/todos')

    return render(request, "deleteList.html",{"form":form})