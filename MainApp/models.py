from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=32)


class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField() 
    description = models.TextField(max_length=900, default="Описание элемента")
    colors = models.ManyToManyField(to=Color)
    
    
    
    def __repr__(self):
        return self.name
