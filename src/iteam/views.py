from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect, render
from django.views.generic.list import ListView

from iteam.models import Order
from . import models


def index(request,gender=None):
    print(gender)
    if gender is None:
        products = models.Product.objects.all()
    else:
        products = models.Product.objects.filter(gender=gender)
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def product_details(request, pk):
    product = models.Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_details.html', context)


def shopping_cart(request, pk):
    cart = models.ShoppingCart.objects.get(pk=pk)
    user = cart.user
    orders = models.Order.objects.filter(cart=cart)
    context = {
        'cart': cart,
        'user': user,
        'orders': orders
    }
    return render(request, 'view_shopping_cart.html', context)


def remove_item(request, pk):
    order = models.Order.objects.get(pk=pk)
    cart = order.cart
    user = cart.user
    if order.quantity == 1:
        order.delete()
    else:
        order.quantity -= 1
        order.save()
    
    orders = models.Order.objects.filter(cart=cart)
    context = {
     'cart': cart,
     'user': user,
     'orders': orders
    }
    return render(request, 'view_shopping_cart.html', context)


def add_item(request,pk_cart,pk_produs):
    cart = models.ShoppingCart.objects.get(pk=pk_cart)
    product = models.Product.objects.get(pk=pk_produs)
    try:
        check_order = models.Order.objects.get(product=product)
    except Order.DoesNotExist:
        order = Order(cart=cart, product=product, quantity=1)
        order.save()
    else:
        check_order.quantity += 1
        check_order.save()    
    orders = models.Order.objects.filter(cart=cart)
    user = cart.user
    context = {
     'cart': cart,
     'user': user,
     'orders': orders
    }
    return render(request, 'view_shopping_cart.html', context)


class EditProfileView(UpdateView):
    model = models.User
