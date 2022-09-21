from django.db import models

# Create your models here.


class Task(models.Model):
    titulo = models.CharField(max_length=100)
    desc = models.CharField(max_length=400, blank=True)
    