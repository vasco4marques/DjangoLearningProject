from django.db import models

# Create your models here.

#Correr no terminal "python manage.py makemigrations" e depois "python manage.py migrate" para o django fazer as alterações à db sem a estragar-mos

# Cada class é uma tabela numa base de dados

# Podem haver funções dentro das classes

# Para adicionar dados com a shell basta (python manage.py shell)
# from myapp.models import ...


# t = ToDoList(name="Algo") # Adiciona uma linha à tabela ToDoList
# t.save()

# Para adicionar um item (como é foreign key) usa-se:
# t.item_set.create(parametros = algo)
# Ex: t.item_set.create(text="Go to the mall", complete=False) 

# Para procurar items na shell podemos usar ToDoList.objects.filter()
# Ex: t = ToDoList.objects
# t.all()
# t.filter(name__startswith="algo")
# Existem muitos destes __filtro 




class ToDoList(models.Model):
    name = models.CharField(max_length=200)
 

    def __str__(self):
        return self.name
    

class Item(models.Model):
    todoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    complete = models.BooleanField()
    
    def __str__(self):
        return self.text


