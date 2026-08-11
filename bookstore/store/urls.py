"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.admin import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('cart/', views.cart_view, name='cart'),  # Kept the session cart view
    path('cart/add/<str:book_title>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<str:book_title>/', views.remove_from_cart, name='remove_from_cart'),  # <-- Added missing comma here
    path('about/', views.about, name='about'),
    path('advdetails/', views.advdetails, name='advdetails'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkoutadv1/', views.checkoutadv1, name='checkoutadv1'),
    path('checkoutadv2/', views.checkoutadv2, name='checkoutadv2'),
    path('checkoutk1/', views.checkoutk1, name='checkoutk1'),
    path('checkoutk2/', views.checkoutk2, name='checkoutk2'),
    path('edudetails/', views.edudetails, name='edudetails'),
    path('fandetails/', views.fandetails, name='fandetails'),
    path('interest/', views.interest, name='interest'),
    path('kiddetails/', views.kiddetails, name='kiddetails'),
    path('login/', views.login, name='login'),
    path('products/', views.products, name='products'),
    path('scidetails/', views.scidetails, name='scidetails'),
    path('signup/', views.signup, name='signup'),
]
