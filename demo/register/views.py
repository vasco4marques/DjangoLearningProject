from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .forms import RegisterForm # ".forms", o ponto serve para indicar que é o forms desta pasta


# Create your views here.

def register(request):
    # Se o request for post guarda-se o novo user na tabela dos users e caso não seja post, cria-se um form vazio.
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("New User saved")
        return redirect("/")
        
    else:
        form = RegisterForm()
    
    return render(request, "register.html", {"form" : form})
