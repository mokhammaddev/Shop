from django.shortcuts import render, redirect
from .forms import AccountCreationForm


def login(request):
    return render(request, 'account/login.html')


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
