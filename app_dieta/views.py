from django.shortcuts import render
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import DadosForm

from django.db.models import Sum, Count

# Create your views here.

def controleDieta(request):

    form = DadosForm
    dados ={
        'forms': form
    }
    return render(request,'index.html', dados)


def telaCadastroUsuario(request):  # aqui carregamos o form com os campos da tabela

    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
    else:
        usuario = 0


    if request.user.is_authenticated:

        usuario = User.objects.get(id=request.user.id)

        dados = {'usuario': usuario,

        }

    else:
        dados = {'usuario': usuario}


    return render(request,'cadastroUsuario.html',dados)


def gravaUsuarioNovo(request):

    if request.method == 'POST':
        if request.user.is_authenticated:

            user_altera = User.objects.get(id=request.user.id);

            user_altera.set_password('senha');

            user_altera.email = request.POST.get('email');
            user_altera.username = request.POST.get('email');
            user_altera.first_name = request.POST.get('primeiro_nome');
            user_altera.last_name = request.POST.get('sobre_nome');

            user_altera.save()

            return redirect('/accounts/logout/');

        else:

            #user = User.objects.create_user('myusername',
            #                                'myemail@crazymail.com',
            #                                'mypassword')
            user_add = User.objects.create_user(request.POST.get('email'),
                                            request.POST.get('email'),
                                            request.POST.get('senha'))

            user_add.first_name = request.POST.get('primeiro_nome');
            user_add.last_name = request.POST.get('sobre_nome');


            user_add.save()

            return redirect('/accounts/login/');