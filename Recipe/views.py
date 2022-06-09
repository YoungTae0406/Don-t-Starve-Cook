from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import meatIngredient
from .models import seafoodIngredient
from .models import vegetableIngredient
from .models import etcIngredient
from .models import fruitIngredient

# Create your views here.

def home(request):
    meats = meatIngredient.objects.all()
    context = {'meatsIngredient': meats}
    return render(request, 'Recipe/mainPage.html', context)

