
from django.contrib import admin
from django.urls import path
from .views import controleDieta

urlpatterns = [
    path('',controleDieta, name ="inicio")
]
