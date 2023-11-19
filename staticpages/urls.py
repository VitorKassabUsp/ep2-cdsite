from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.about, name='about'), #link para about.html
    path('', views.index, name='index'),
]