from django.shortcuts import render
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.db.models import Sum, Count

# Create your views here.

def controleDieta(request):

    return render(request,'index.html')
