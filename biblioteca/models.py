from django.db import models

# Create your models here.
class Escritor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
   
    def __str__(self):
        return self.nome
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    escritor = models.ForeignKey(Escritor, on_delete=models.CASCADE)
    data_publicacao = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
   
    def __str__(self):
        return self.titulo
