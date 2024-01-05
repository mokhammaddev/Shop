from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Shop, Size, Category, Sale, SoldShop
from blog.models import Blog


def navbar(request):
    all_price_sold_shop = number_sold_shop = 0
    if request.user.is_authenticated:
        sold_shops = SoldShop.objects.order_by('-id')
        for shop_one in sold_shops:
            if shop_one.account == request.user:
                number_sold_shop += 1
                all_price_sold_shop += shop_one.shop.price
    ctx = {
        'all_price_sold_shop': all_price_sold_shop,
        'number_sold_shop': number_sold_shop,
    }
    return render(request, 'nav.html', ctx)


def footer(request):
    return render(request, 'footer.html')


def index(request):
    last_one_shop = last_two_shop = last_three_shop = sale = sale_money = sale_time = None
    shops = Shop.objects.order_by('-id')
    blogs = Blog.objects.order_by('-id')

    # if last_one_shop and last_two_shop and last_three_shop:
    #     last_one_shop = Shop.objects.order_by('-id')[0]
    #     last_two_shop = Shop.objects.order_by('-id')[1]
    #     last_three_shop = Shop.objects.order_by('-id')[2]
    if sale:
        sale = Sale.objects.order_by('-id')[0]
        sale_money = sale.shop.price*(sale.percent/100)
        sale_time = sale.end_date - sale.start_date
    page_number = request.GET.get('page', 1)
    paginator = Paginator(shops, 8)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    page_number_blog = request.GET.get('page', 1)
    paginator = Paginator(blogs, 8)
    try:
        page_obj_blog = paginator.page(page_number_blog)
    except PageNotAnInteger:
        page_obj_blog = paginator.page(1)
    except EmptyPage:
        page_obj_blog = paginator.page(1)
    ctx = {
        'shops': page_obj,
        'blogs': page_obj_blog,
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
        shops = shops.filter(title__icontains=search)
    if cat:
        shops = shops.filter(category__title__exact=cat)
    if size:
        shops = shops.filter(size__title__exact=size)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(shops, 3)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        'shops': page_obj,
        'categories': categories,
        'sizes': sizes,
    }
    return render(request, 'shop/shop.html', ctx)


def shop_detail(request, pk):
    shop_object = get_object_or_404(Shop, id=pk)
    last_objects = Shop.objects.order_by('-id')[:4]
    shops = Shop.objects.order_by('-id')
    sizes = Size.objects.all()
    ctx = {
        'shop': shop_object,
        'last_objects': last_objects,
        'sizes': sizes,
    }
    return render(request, 'shop/shop-details.html', ctx)


def shopping(request):
    sold_one_shop = []
    all_price_sold_shop = number_sold_shop = 0
    if request.user.is_authenticated:
        sold_shops = SoldShop.objects.order_by('-id')
        for shop_one in sold_shops:
            if shop_one.account == request.user:
                sold_one_shop.append(shop_one)
                number_sold_shop += 1
                all_price_sold_shop += shop_one.shop.price
    ctx = {
        'sold_shops': sold_one_shop,
        'all_price_sold_shop': all_price_sold_shop,
        'number_sold_shop': number_sold_shop,
    }
    return render(request, 'shop/shopping-cart.html', ctx)


def checkout(request, pk):
    return render(request, 'shop/checkout.html')
