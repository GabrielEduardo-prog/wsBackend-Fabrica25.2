from django.urls import path
from . import views

app_name = 'biblioteca'

urlpatterns = [
    path('', views.LivroList.as_view(), name='livro_list'),
    path('livro/', views.LivroList.as_view(), name='livro_list'),
    path('livro/<int:pk>/', views.LivroDetail.as_view(), name='livro_detail'),
    path('livro/create/', views.LivroCreate.as_view(), name='livro_create'),
    path('livro/<int:pk>/edit/', views.LivroUpdate.as_view(), name='livro_edit'),
    path('livro/<int:pk>/delete/', views.LivroDelete.as_view(), name='livro_delete'),
    
    path('escritor/', views.EscritorList.as_view(), name='escritor_list'),
    path('escritor/create/', views.EscritorCreate.as_view(), name='escritor_create'),
    path('escritor/<int:pk>/edit/', views.EscritorUpdate.as_view(), name='escritor_edit'),
    path('escritor/<int:pk>/delete/', views.EscritorDelete.as_view(), name='escritor_delete'),
]