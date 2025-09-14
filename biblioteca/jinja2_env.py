from jinja2 import Environment
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage


def environment(**options):
    """
    Configuração do ambiente Jinja2 para Django
    """
    env = Environment(**options)
    
    # Adicionar funções globais do Django para Jinja2
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    
    return env