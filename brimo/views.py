from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    ctx = {'at_home': True}
    return render(request, 'brimo/home.djhtml', ctx)


def about(request):
    ctx = {'at_about': True}
    return render(request, 'brimo/about.djhtml', ctx)
