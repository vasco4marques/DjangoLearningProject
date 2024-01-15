from django.db import models

# Create your models here.

#Correr no terminal "python manage.py makemigrations" e depois "python manage.py migrate" para o django fazer as alterações à db sem a estragar-mos

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


