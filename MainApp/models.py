from django.db import models

# Create your models here.
#

class Color(models.Model):
   name = models.TextField(max_length=30)
   def __repr__(self):
      return f'Color({self.name})'

class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()
   description = models.TextField(max_length=1000, default="Базовое описание")
   color = models.ManyToManyField(to=Color)
