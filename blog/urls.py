from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog-detail'),
    path('contact/', views.contact, name='contact'),
]
