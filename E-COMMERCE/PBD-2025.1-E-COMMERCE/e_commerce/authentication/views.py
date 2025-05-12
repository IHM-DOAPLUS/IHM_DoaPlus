from django.shortcuts import render
from .forms import UserLoginForm, UserRegistration 
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout


def user_page(request):
    form = UserRegistration()
    return render(request, 'user.html', {'form': form})

def login_page(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user=user)
                return redirect('ecommerce:home')
    context = {'form': form}
    return render(request, 'login.html', context)

def handle_logout(request):
    logout(request)
    return redirect('authentication:login')
