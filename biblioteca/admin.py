from django.contrib import admin
from .models import Escritor, Livro


@admin.register(Escritor)
class EscritorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)
    ordering = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'escritor', 'data_publicacao', 'isbn')
    search_fields = ('titulo', 'isbn', 'escritor__nome')
    list_filter = ('data_publicacao', 'escritor')
    date_hierarchy = 'data_publicacao'
    ordering = ('-data_publicacao',)
    
   
    fields = ('titulo', 'escritor', 'data_publicacao', 'isbn')
    
    
    autocomplete_fields = ['escritor']
