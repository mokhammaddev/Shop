from django.shortcuts import render, redirect, get_object_or_404
from . models import Blog
from shop.models import Shop
from .forms import ContactForm


def about(request):
    return render(request, 'blog/about.html')


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
    return render(request, 'blog/contact.html', ctx)


def blog(request):
    blogs = Blog.objects.order_by('-id')
    ctx = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', ctx)


def blog_detail(request, pk):
    blog_one_detail = get_object_or_404(Blog, id=pk)
    ctx = {
        'blog': blog_one_detail,
    }
    return render(request, 'blog/blog-details.html', ctx)

