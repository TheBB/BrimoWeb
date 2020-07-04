from django.shortcuts import render
from django.http import HttpResponse, FileResponse

from .models import *


def base_context(path):
    return {
        'categories': PortfolioCategory.objects.all(),
        'path': path.split('/')
    }


def home(request):
    ctx = base_context(path='home')
    return render(request, 'brimo/home.djhtml', ctx)


def about(request):
    ctx = base_context(path='about')
    return render(request, 'brimo/about.djhtml', ctx)


def portfolio_item(request, juxid):
    ctx = base_context(path='portfolio')
    ctx['jux'] = Juxtaposition.objects.get()
    return render(request, 'brimo/portfolio_item.djhtml', ctx)


def portfolio(request):
    ctx = base_context(path='portfolio')
    return render(request, 'brimo/portfolio_categories.djhtml', ctx)


def portfolio_category(request, catid, slug=None):
    ctx = base_context(path='portfolio')
    ctx['category'] = PortfolioCategory.objects.get(id=catid)
    return render(request, 'brimo/portfolio_category.djhtml', ctx)


def image(request, imageid):
    img = Image.objects.get(id=imageid)
    return FileResponse(img.imagefile)


def juxtapose(request, juxid):
    jux = Juxtaposition.objects.get(id=juxid)
    return render(request, 'brimo/juxtapose.djhtml', {'jux': jux})
