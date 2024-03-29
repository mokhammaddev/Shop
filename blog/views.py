from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from . models import Blog, Comment
from shop.models import Shop, SoldShop
from .forms import ContactForm, CommentForm


def about(request):
    all_price_sold_shop = number_sold_shop = 0
    sold_one_shop = SoldShop.objects.all()
    for sold_shop in sold_one_shop:
        all_price_sold_shop += sold_shop.shop.price
        number_sold_shop += 1
    ctx = {
        'all_price_sold_shop': all_price_sold_shop,
        'number_sold_shop': number_sold_shop,
    }
    return render(request, 'blog/about.html', ctx)


def contact(request):
    all_price_sold_shop = number_sold_shop = 0
    sold_one_shop = SoldShop.objects.all()
    for sold_shop in sold_one_shop:
        all_price_sold_shop += sold_shop.shop.price
        number_sold_shop += 1
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    ctx = {
        'form': form,
        'all_price_sold_shop': all_price_sold_shop,
        'number_sold_shop': number_sold_shop,
    }
    return render(request, 'blog/contact.html', ctx)


def blog_views(request):
    all_price_sold_shop = number_sold_shop = 0
    sold_one_shop = SoldShop.objects.all()
    for sold_shop in sold_one_shop:
        all_price_sold_shop += sold_shop.shop.price
        number_sold_shop += 1
    blogs = Blog.objects.order_by('-id')
    page_number = request.GET.get('page', 1)
    paginator = Paginator(blogs, 3)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        'blogs': page_obj,
        'all_price_sold_shop': all_price_sold_shop,
        'number_sold_shop': number_sold_shop,
    }
    return render(request, 'blog/blog.html', ctx)


def blog_detail(request, pk):
    all_price_sold_shop = number_sold_shop = 0
    sold_one_shop = SoldShop.objects.all()
    for sold_shop in sold_one_shop:
        all_price_sold_shop += sold_shop.shop.price
        number_sold_shop += 1
    blog_one_detail = get_object_or_404(Blog, id=pk)
    comments = Comment.objects.filter(blog_id=pk)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if not request.user.is_authenticated:
            return redirect('login')
        if comment_form.is_valid():
            message = request.POST.get('message')
            blog = blog_one_detail
            author_id = request.user.id
            if blog:
                obj = Comment(message=message, blog_id=pk, author_id=author_id)
                obj.save()
            return redirect(reverse('blog-detail', kwargs={"pk": pk}))
    ctx = {
        "comment_form": comment_form,
        "comments": comments,
        'blog': blog_one_detail,
        'all_price_sold_shop': all_price_sold_shop,
        'number_sold_shop': number_sold_shop,
    }
    return render(request, 'blog/blog-details.html', ctx)
