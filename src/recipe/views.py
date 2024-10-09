from django.shortcuts import render
from .data import recipies

# Create your views here.
def recipe(request):
    recipe = recipies[0]
    return render(request, 'recipe/index.html', context={"recipe": recipe})