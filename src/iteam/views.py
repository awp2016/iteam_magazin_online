from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect, render

from . import models

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def shopping_cart(request, pk):
    cart = models.ShoppingCart.objects.get(pk=pk)
    user = cart.user
    orders = Order.objects.get(cart=cart)
    context = {
        'cart': cart,
        'user': user,
        'orders': orders
    }
    return render(request, 'view_shopping_cart.html', context)

def remove_item(request, pk):
    order = models.Order.objects.get(pk=pk)
    if order.quantity == 1:
        order.delete()
    else:
        order.quantity -= 1
    order.save()
    cart = order.cart
    user = cart.user
    orders = Order.objects.get(cart=cart)
    context = {
     'cart': cart,
     'user': user,
     'orders': orders
    }
    return render(request, 'view_shopping_cart.html', context)

def add_item(request,pk_cart,pk_product,quantity):
    cart = models.ShoppingCart.objects.get(pk=pk_cart)
    product = models.Product.objects.get(pk=pk_product)
    order = Order(cart=cart, product=product, quantity=quantity)
    order.save()
    orders = Order.objects.get(cart=cart)
    user = cart.user
    context = {
     'cart': cart,
     'user': user,
     'orders': orders
    }
    return render(request, 'view_shopping_cart.html', context)


class EditProfileView(UpdateView):
    model = models.User
