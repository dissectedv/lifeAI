from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já está em uso.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email já está em uso.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                messages.success(request, 'Usuário registrado com sucesso!')
                return redirect('main_page')
        else:
            messages.error(request, 'Todos os campos são obrigatórios.')

    return render(request, 'lifeAI/index.html')

@login_required
def main_page(request):
    return render(request, 'lifeAI/main_page.html')
