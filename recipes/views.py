from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.http import Http404
from utils.recipes.factory import make_recipe
from .models import Recipe

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
    
def category(request, category_id):
   recipes = get_list_or_404(Recipe.objects.filter(category_id=category_id, is_published=True)).order_by('-id')
   return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title':  f'Categoria: {recipes.first().category.name}'
    })    
    
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })



