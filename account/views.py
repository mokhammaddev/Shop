from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AccountCreationForm, AccountLoginForm
from django.contrib.auth import authenticate, logout, login


def login_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        print(1111111, name, password)
        user = authenticate(request, name=name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login O'xshadi")
            return redirect('index')
        else:
            messages.error(request, "Login o'xshamadi")
            return redirect('/')
    ctx = {
        # 'form': form,
    }
    return render(request, 'account/login.html', ctx)


def logout_page(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')
    # if request.user.is_authenticated:
    #     logout(request)
    #     print("Logout bo'ldi")
    #     messages.success(request, "Logout o'xshadi")
    #     return redirect('index')
    return render(request, 'account/logout.html')


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
