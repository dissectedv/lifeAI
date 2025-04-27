from django.shortcuts import render
from django.conf import settings 

def index(request):
    return render(request, 'lifeAI/index.html')

def main_page(request):
    return render(request, 'lifeAI/main_page.html', {'DEBUG': settings.DEBUG})
