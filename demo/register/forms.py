from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    # O css deste form vem do CrispyForms instalado pelo comando "pip install django-crispy-forms". Depois temos de ir ao settings.py e colocar "crispy_forms" nas installed apps e adicionar esta variavel : "CRISPY_TEMPLATE_PACK = "bootstrap5""
    CRISPY_TEMPLATE_PACK = "bootstrap5"
    # Cada vez que guardarmos RegisterForm temos que guardar no model User estes dados
    class Meta:
        model = User
        # Esta lista de campos contém a ordem pelos quais os fields do form vão ser listados
        fields = ["username","email","password1","password2"]





 