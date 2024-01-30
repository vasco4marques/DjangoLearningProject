from django import forms

# Criar um form com os dados do model em questão
# Cada class é um form

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200) #label é o que vai estar escrito no form antes de preencher
    check = forms.BooleanField(required = False)

class deleteList(forms.Form):
    name = forms.CharField(label = "Name to delete", max_length=200)


    


    