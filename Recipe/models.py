from django.db import models

# Create your models here.
class cookResult(models.Model):
    name = models.CharField(max_length=30)


class meatIngredient(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField()
    img = models.ImageField()

class vegetableIngredient(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField()
    img = models.ImageField()

class fruitIngredient(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField()
    img = models.ImageField()

class seafoodIngredient(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField()
    img = models.ImageField()

class etcIngredient(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField(default=1)
    img = models.ImageField()
