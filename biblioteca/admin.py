from django.contrib import admin
from .models import Escritor, Livro

# Configuração do Admin para Escritor
@admin.register(Escritor)
class EscritorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)
    ordering = ('nome',)

# Configuração do Admin para Livro
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'escritor', 'data_publicacao', 'isbn')
    search_fields = ('titulo', 'isbn', 'escritor__nome')
    list_filter = ('data_publicacao', 'escritor')
    date_hierarchy = 'data_publicacao'
    ordering = ('-data_publicacao',)
    
    # Campos no formulário de edição
    fields = ('titulo', 'escritor', 'data_publicacao', 'isbn')
    
    # Para facilitar a seleção do escritor
    autocomplete_fields = ['escritor']
