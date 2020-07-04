from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio/category/<int:catid><str:slug>', views.portfolio_category, name='portfolio_category'),
    path('image/<int:imageid>', views.image, name='image'),
    path('juxtapose/<int:juxid>', views.juxtapose, name='juxtapose'),
]
