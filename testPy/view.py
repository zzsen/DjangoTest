from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world !！ ")


def hi(request):
    context = {'hello': 'Hello World!',
               'hi': 'emmm'}
    return render(request, 'hello.html', context)
