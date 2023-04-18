from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Это главная страница Yatube')

def group_posts(request, pk):
    return HttpResponse(f'Это страница сообщества {pk}')

# Create your views here.
