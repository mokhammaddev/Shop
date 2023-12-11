from django.shortcuts import render, get_object_or_404
from .models import Shop, Size, Category, Sale
from blog.models import Blog


def index(request):
    last_one_shop = last_two_shop = last_three_shop = sale = sale_money = sale_time = None
    shops = Shop.objects.order_by('-id')
    blogs = Blog.objects.order_by('-id')
    if last_one_shop and last_two_shop and last_three_shop:
        last_one_shop = Shop.objects.order_by('-id')[0]
        last_two_shop = Shop.objects.order_by('-id')[1]
        last_three_shop = Shop.objects.order_by('-id')[2]
    if sale:
        sale = Sale.objects.order_by('-id')[0]
        sale_money = sale.shop.price*(sale.percent/100)
        sale_time = sale.end_date - sale.start_date
    ctx = {
        'shops': shops,
        'blogs': blogs,
        'last_one_shop': last_one_shop,
        'last_two_shop': last_two_shop,
        'last_three_shop': last_three_shop,
        'sale': sale,
        'sale_time': sale_time,
        'sale_money': sale_money,
    }
    return render(request, 'shop/index.html', ctx)


def shop(request):
    shops = Shop.objects.order_by('-id')
    categories = Category.objects.all()
    sizes = Size.objects.all()
    cat = request.GET.get('cat')
    size = request.GET.get('size')
    prc = request.GET.get('prc')
    search = request.GET.get('search')
    if search:
        shops = request.GET.get('search')
    if cat:
        shops = shops.filter(category__title__exact=cat)
    if size:
        shops = shops.filter(size__title__exact=size)
    if prc:
        shops = shops.filter(price__exact=prc)
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
