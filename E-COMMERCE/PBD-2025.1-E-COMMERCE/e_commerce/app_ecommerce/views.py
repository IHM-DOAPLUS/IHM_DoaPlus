from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import RegisterItem, RegisterCompany
from .models import Company, Itens


def index(request):
    return render(request, 'index.html')


def sales_dashboard(request):
    return render(request, 'sales_dashboard.html')

@login_required
def dash(request):
    return render(request, 'dash.html')


def create_item(request):
    form = RegisterItem()
    if request.method == 'POST':
        form = RegisterItem(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ecommerce:sales_dashboard')
    else:
        form = RegisterItem()
    contex = {'form': form}
    return render(request, 'create_item.html', contex)


def list_companies(request):
    companies = Company.objects.all().order_by('name')
    contex = {'companies': companies}
    return render(request, 'list_companies.html', contex)


def list_itens(request):
    itens = Itens.objects.all().order_by('name')
    contex = {'itens': itens}
    return render(request, 'list_itens.html', contex)


def create_company(request):
    form = RegisterCompany()
    if request.method == 'POST':
        form = RegisterCompany(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('authentication:login')
    else:
        form = RegisterCompany()
    contex = {'form': form}
    return render(request, 'create_company.html', contex)
