from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AccountCreationForm, AccountLoginForm
from django.contrib.auth import authenticate, logout, login


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        return redirect('login')
    # return render(request, 'account/login.html')
    return render(request, 'account/login_new.html')


def logout_page(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')
    return render(request, 'account/logout.html')


def sign(request):
    form = AccountCreationForm()
    if request.method == 'POST':
        form = AccountCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        messages.error("Login failed")

    ctx = {
        'form': form,
    }
    return render(request, 'account/sign.html', ctx)
