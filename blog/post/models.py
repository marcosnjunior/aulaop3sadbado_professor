from django.db import models
from django.contrib.auth.models import User


# Modelo Autor
class Autor(models.Model):

    nome = models.CharField(max_length=100)
    sobre = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
# Modelo Categoria
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

# Modelo Post
class Post(models.Model):
    
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

# Modelo Comentário
class Comentario(models.Model):

    autor = models.CharField(max_length=100)
    email = models.EmailField()
    corpo = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return f'Comentário de {self.autor} em {self.post.titulo}'

