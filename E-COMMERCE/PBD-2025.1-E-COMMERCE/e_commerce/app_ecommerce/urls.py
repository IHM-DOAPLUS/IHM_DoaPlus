from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.index, name='index'),
    path('sales_dashboard/', views.sales_dashboard, name='sales_dashboard'),
    path('dash/', views.dash, name='dash'),
    path('create_item/', views.create_item, name='Create_item'),
    path('list_companies/', views.list_companies, name='list_companies'),
    path('list_itens/', views.list_itens, name='list_itens'),

]
