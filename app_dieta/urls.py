
from django.contrib import admin
from django.urls import path
from .views import controleDieta, telaCadastroUsuario, gravaUsuarioNovo

urlpatterns = [
    path('',controleDieta, name ="inicio"),
    path('tela-usuario/',telaCadastroUsuario, name="TelaCadastroUsuario"),
    path('grava-usuario-novo/',gravaUsuarioNovo, name='GravaUsuarioNovo'),
]
