from django.db import models

class Dish(models.Model):
   name = models.CharField(max_length=100, default="No Name")
   description = models.CharField(max_length=1000, default="No Description")
   category = models.CharField(max_length=100, default="Uncategorized")
   price = models.PositiveIntegerField(default=0)
   image = models.ImageField(upload_to='', default='default_dish.jpg')
