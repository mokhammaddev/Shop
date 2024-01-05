from django.urls import path
from . import views

urlpatterns = [
    path('navbar/', views.navbar, name='navbar'),
    path('footer/', views.footer, name='footer'),
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:pk>/', views.shop_detail, name='shop-detail'),
    path('shopping/', views.shopping, name='shopping'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
]
