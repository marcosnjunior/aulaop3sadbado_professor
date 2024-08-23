from django.contrib import admin
from .models import Categoria, Post, Comentario, Autor

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobre')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao', 'publicado')
    list_filter = ('publicado', 'data_publicacao')
    search_fields = ('titulo', 'conteudo')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'data_comentario', 'aprovado')
    list_filter = ('aprovado', 'data_comentario')
    search_fields = ('autor', 'corpo')
