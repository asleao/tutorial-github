from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
import requests
from django.shortcuts import redirect

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def cria_repositorio_github(token, nome, linguagem):
    r = requests.post('http://localhost:8001/cria_repositorio/', data={'nome_repositorio':nome, 'token':token, 'linguagem':linguagem})
    print(r)
@login_required
def criar_repositorio(request):
    if request.method == 'POST':
        form = formRepositorio(request.POST)
        if form.is_valid():
            user = request.user
            token = user.social_auth.get(provider='github').access_token
            nome_repositorio = form.cleaned_data['nome']
            linguagem = form.cleaned_data['linguagem']
            print(token)
            r = cria_repositorio_github(token, nome_repositorio, linguagem)
            return redirect('home')
    else:
        form = formRepositorio()
    return render(request, 'repositorio.html', {'form':form})