from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Escritor, Livro
from .forms import EscritorForm, LivroForm

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
