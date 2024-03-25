from django.db import models
from django.contrib.auth.models import User

#Tabela de categorias#
class Category(models.Model):
    name = models.CharField(max_length=65)
    
    def __str__(self):
        return self.name

#Tabela de receita#
class Recipe(models.Model):
    #Colunas da tabela#
    #Coluna de titulo#
    title = models.CharField(max_length=65)
    #Coluna de descrição#
    description = models.CharField(max_length=165)
    #Coluna de slug#
    slug = models.SlugField()
    #Coluna de tempo de preparação#
    preparation_time = models.IntegerField()
    #Unidade de tempo da preparação#
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(
            Category, on_delete=models.SET_NULL, null=True, blank=True, default=None,
        )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    
    def __str__(self):
        return self.title
