from django.shortcuts import render, redirect
from . models import Blog
from shop.models import Shop
from .forms import ContactForm


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    ctx = {
        'form': form,
    }
    return render(request, 'shop/contact.html', ctx)


def blog(request):
    return render(request, 'shop/blog.html')


def blog_detail(request, pk):
    return render(request, 'shop/blog-details.html')

