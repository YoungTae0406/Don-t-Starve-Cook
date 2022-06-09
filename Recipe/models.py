from django.db import models

# Create your models here.
class cookResult(models.Model):
    name = models.CharField(max_length=30)
    hunger = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    mentality = models.IntegerField(default=0)
    img = models.ImageField(null=True, upload_to="", blank=True)



class meatIngredient(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField(default = 0)
    img = models.ImageField(null=True, upload_to="", blank=True)

class vegetableIngredient(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField(default=0)
    img = models.ImageField(null=True, upload_to="", blank=True)

class fruitIngredient(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField(default=0)
    img = models.ImageField(null=True, upload_to="", blank=True)

class seafoodIngredient(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField(default = 0)
    img = models.ImageField(null=True, upload_to="", blank=True)

class etcIngredient(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField(default=0)
    img = models.ImageField(null=True, upload_to="", blank=True)
