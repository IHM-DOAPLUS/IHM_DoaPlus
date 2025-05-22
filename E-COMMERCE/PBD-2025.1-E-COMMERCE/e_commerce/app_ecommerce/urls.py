from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.index, name='index'),
    path('portifolio/', views.portifolio, name='portifolio'),
    path('starter/', views.starter_page, name='starter'),
    path('service/', views.service, name='service'),
    path('login/dash/', views.dash, name='dash'),
    path('user/', views.user, name='user'),
    path('item/', views.item, name='item'),







]
