from django.shortcuts import render


def about(request):
    return render(request, 'shop/about.html')


def blog(request):
    return render(request, 'shop/blog.html')


def blog_detail(request, pk):
    return render(request, 'shop/blog-details.html')


def contact(request):
    return render(request, 'shop/contact.html')
