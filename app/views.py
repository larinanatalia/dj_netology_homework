import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    current_dir = os.getcwd()
    workdir_list = os.listdir(path= current_dir)
    total = []
    for i in workdir_list:
        if len(total) == len(workdir_list) - 1:
            total.append(f'\n - {i}.')
        else:
            total.append(f'\n - {i},')
    return HttpResponse(total)
