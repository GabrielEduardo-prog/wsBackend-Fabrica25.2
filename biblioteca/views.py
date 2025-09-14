from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from datetime import datetime
import json

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Escritor, Livro
from .forms import EscritorForm, LivroForm
from .services import GoogleBooksService

class EscritorList(ListView):
    model = Escritor
    template_name = 'escritor_list.html'

class EscritorCreate(CreateView):
    model = Escritor
    form_class = EscritorForm
    template_name = 'escritor_form.html'
    success_url = reverse_lazy('biblioteca:escritor_list')

class EscritorUpdate(UpdateView):
    model = Escritor
    form_class = EscritorForm
    template_name = 'escritor_form.html'
    success_url = reverse_lazy('biblioteca:escritor_list')

class EscritorDelete(DeleteView):
    model = Escritor
    template_name = 'escritor_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:escritor_list')

class LivroList(ListView):
    model = Livro
    template_name = 'livro_list.html'

class LivroDetail(DetailView):
    model = Livro
    template_name = 'livro_detail.html'

class LivroCreate(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livro_form.html'
    success_url = reverse_lazy('biblioteca:livro_list')

class LivroUpdate(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livro_form.html'
    success_url = reverse_lazy('biblioteca:livro_list')

class LivroDelete(DeleteView):
    model = Livro
    template_name = 'livro_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:livro_list')


# Views para API Externa
def buscar_livros_api(request):
    """
    View para buscar livros na API do Google Books
    """
    if request.method == 'GET':
        return render(request, 'buscar_livros_api.html')
    
    elif request.method == 'POST':
        query = request.POST.get('query', '').strip()
        if not query:
            messages.error(request, 'Digite um termo para buscar.')
            return render(request, 'buscar_livros_api.html')
        
        # Buscar livros na API
        livros = GoogleBooksService.buscar_livros(query, max_results=20)
        
        if not livros:
            messages.warning(request, 'Nenhum livro encontrado para este termo.')
        
        return render(request, 'buscar_livros_api.html', {
            'livros': livros,
            'query': query
        })


@require_http_methods(["POST"])
def importar_livro_api(request):
    """
    View para importar um livro específico da API para o banco local
    """
    try:
        # Receber dados do livro via POST
        livro_data = {
            'titulo': request.POST.get('titulo'),
            'autor': request.POST.get('autor'),
            'isbn': request.POST.get('isbn'),
            'data_publicacao': request.POST.get('data_publicacao'),
        }
        
        # Converter data_publicacao para objeto date se presente
        if livro_data['data_publicacao']:
            from datetime import datetime
            try:
                livro_data['data_publicacao'] = datetime.strptime(
                    livro_data['data_publicacao'], '%Y-%m-%d'
                ).date()
            except ValueError:
                livro_data['data_publicacao'] = None
        
        # Importar livro
        livro, mensagem = GoogleBooksService.importar_livro(livro_data)
        
        if livro:
            messages.success(request, f'Livro "{livro.titulo}" importado com sucesso!')
        else:
            messages.error(request, mensagem)
            
    except Exception as e:
        messages.error(request, f'Erro ao importar livro: {str(e)}')
    
    return redirect('biblioteca:buscar_livros_api')


def relatorio_biblioteca(request):
    """
    View que gera relatório da biblioteca usando Jinja2
    """
    from django.http import HttpResponse
    
    # Coletar dados para o relatório
    livros = Livro.objects.select_related('escritor').all()
    autores = Escritor.objects.prefetch_related('livro_set').all()
    
    # Calcular estatísticas
    total_livros = livros.count()
    total_autores = autores.count()
    livros_com_isbn = livros.exclude(isbn='').exclude(isbn__isnull=True).count()
    
    # Contexto para o template Jinja2
    context = {
        'livros': livros,
        'autores': autores,
        'total_livros': total_livros,
        'total_autores': total_autores,
        'livros_com_isbn': livros_com_isbn,
        'data_geracao': datetime.now(),
    }
    
    # Carregar template Jinja2 e renderizar
    template = loader.get_template('relatorio_biblioteca.html')
    html_content = template.render(context, request)
    
    return HttpResponse(html_content)
