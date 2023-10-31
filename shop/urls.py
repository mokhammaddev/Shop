from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:pk>/', views.shop_detail, name='shop-detail'),
    path('shopping/<int:pk>/', views.shopping, name='shopping'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
]
