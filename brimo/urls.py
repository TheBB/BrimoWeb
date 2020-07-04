from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('portfolio/<int:juxid>', views.portfolio_item, name='portfolio_item'),
    path('image/<int:imageid>', views.image, name='image'),
    path('juxtapose/<int:juxid>', views.juxtapose, name='juxtapose'),
]
