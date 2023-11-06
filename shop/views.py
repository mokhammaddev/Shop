from django.shortcuts import render, get_object_or_404
from .models import Shop, Size, Category
from blog.models import Blog


def index(request):
    shops = Shop.objects.order_by('-id')
    blogs = Blog.objects.order_by('-id')
    # last_one_shop = Shop.objects.order_by('-id')[0]
    # last_two_shop = Shop.objects.order_by('-id')[1]
    # last_three_shop = Shop.objects.order_by('-id')[2]
    ctx = {
        'shops': shops,
        'blogs': blogs,
        # 'last_one_shop': last_one_shop,
        # 'last_two_shop': last_two_shop,
        # 'last_three_shop': last_three_shop,
    }
    return render(request, 'shop/index.html', ctx)


def shop(request):
    shops = Shop.objects.order_by('-id')
    categories = Category.objects.all()
    sizes = Size.objects.all()
    ctx = {
        'shops': shops,
        'categories': categories,
        'sizes': sizes,
    }
    return render(request, 'shop/shop.html', ctx)


def shop_detail(request, pk):
    shop_object = get_object_or_404(Shop, id=pk)
    last_objects = Shop.objects.order_by('-id')[:4]
    shops = Shop.objects.order_by('-id')

    ctx = {
        'shop': shop_object,
        'last_objects': last_objects,
    }
    return render(request, 'shop/shop-details.html', ctx)


def shopping(request, pk):
    cart = get_object_or_404(Shop, id=pk)
    ctx = {
        'cart': cart,
    }
    return render(request, 'shop/shopping-cart.html', ctx)


def checkout(request, pk):
    return render(request, 'shop/checkout.html')
