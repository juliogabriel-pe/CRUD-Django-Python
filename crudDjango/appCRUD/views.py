from django.shortcuts import render
from .models import *

def home(request):
    return render(request,'home.html')

def cadastro(request):
    return render(request,'cadastro.html')

def listagem(request):
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()
    dadosUsuarios = {
        'usuarios' : Usuarios.objects.all()
    }
    return render(request, 'listagemUsuarios.html',dadosUsuarios)
