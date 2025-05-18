from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def portifolio(request):
    return render(request, 'portfolio-details.html')


def starter_page(request):
    return render(request, 'starter-page.html')


def service(request):
    return render(request, 'service-details.html')

def dash(request):
    return render(request, 'dash.html')

def user(request):
    return render(request, 'user.html')
