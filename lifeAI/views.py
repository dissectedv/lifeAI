from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def register_view(request):
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
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                login(request, user)
                messages.success(request, 'Usuário registrado com sucesso!')
                return redirect('main_page.html')
        else:
            messages.error(request, 'Todos os campos são obrigatórios.')

    return render(request, 'lifeAI/index.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            username = User.objects.get(email=email).username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_page')
            else:
                messages.error(request, 'Credenciais inválidas.')
        except User.DoesNotExist:
            messages.error(request, 'Usuário não encontrado.')
    return redirect('register_view')


def main_page(request):
    if not request.user.is_authenticated:
        return redirect('login_view')
    return render(request, "LifeAI/main_page.html", {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect('register_view')
