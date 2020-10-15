
from django.contrib import admin
from django.urls import path
from .views import controleDieta, telaCadastroUsuario, gravaUsuarioNovo, gravaDados

urlpatterns = [
    path('',controleDieta, name ="inicio"),
    path('tela-usuario/',telaCadastroUsuario, name="TelaCadastroUsuario"),
    path('grava-usuario-novo/',gravaUsuarioNovo, name='GravaUsuarioNovo'),
    path('grava-dados/',gravaDados, name='GravaDados'),
]
