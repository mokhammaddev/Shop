from django.shortcuts import render, redirect
from .forms import AccountCreationForm, AccountLoginForm


def login(request):
    form = AccountLoginForm()
    if request.method == 'POST':
        form = AccountLoginForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    ctx = {
        'form': form,
    }
    return render(request, 'account/login.html', ctx)


def sign(request):
    form = AccountCreationForm()
    if request.method == 'POST':
        form = AccountCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    ctx = {
        'form': form,
    }
    return render(request, 'account/sign.html', ctx)
