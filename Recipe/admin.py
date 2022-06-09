from django.contrib import admin
from .models import cookResult, meatIngredient, vegetableIngredient\
    , fruitIngredient, seafoodIngredient
# Register your models here.

admin.site.register(cookResult)
admin.site.register(meatIngredient)
admin.site.register(vegetableIngredient)
admin.site.register(fruitIngredient)
admin.site.register(seafoodIngredient)

