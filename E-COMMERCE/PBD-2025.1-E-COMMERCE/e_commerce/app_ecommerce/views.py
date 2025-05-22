from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import RegisterItem


def index(request):
    return render(request, 'index.html')


def portifolio(request):
    return render(request, 'portfolio-details.html')


def starter_page(request):
    return render(request, 'starter-page.html')


def service(request):
    return render(request, 'service-details.html')


@login_required
def dash(request):
    return render(request, 'dash.html')


def user(request):
    return render(request, 'user.html')


def item(request):
    form = RegisterItem()
    if request.method == 'POST':
        form = RegisterItem(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ecommerce:item')
    else:
        form = RegisterItem()
    contex = {'form': form}
    return render(request, 'item.html', contex)
