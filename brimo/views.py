from django.shortcuts import render
from django.http import HttpResponse, FileResponse

from .models import Image, Juxtaposition


def home(request):
    ctx = {'at_home': True}
    return render(request, 'brimo/home.djhtml', ctx)


def about(request):
    ctx = {'at_about': True}
    return render(request, 'brimo/about.djhtml', ctx)


def portfolio_item(request, juxid):
    jux = Juxtaposition.objects.get(id=juxid)
    ctx = {'at_portfolio': True, 'jux': jux}
    return render(request, 'brimo/portfolio_item.djhtml', ctx)


def image(request, imageid):
    img = Image.objects.get(id=imageid)
    return FileResponse(img.imagefile)


def juxtapose(request, juxid):
    jux = Juxtaposition.objects.get(id=juxid)
    return render(request, 'brimo/juxtapose.djhtml', {'jux': jux})
