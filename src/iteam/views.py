from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect, render
from django.views.generic.list import ListView

from iteam.models import Order
from . import models

class ProductsListView(ListView):
    model = models.Product
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        products = self.model.objects.all()
        context['products'] = products
        return context

    def get_queryset(self):
        return self.model.objects.order_by('-price')

def index(request):
    products = models.Product.objects.all()
    tup = []
    for prod in products:
        image = models.Image.objects.filter(product=prod).first
        tuplu = (prod, image)
        tup.append(tuplu)
    context = {
        'tuplu': tup
    }
    return render(request, 'index.html', context)

def product_details(request, pk):
    product = models.Product.objects.get(pk=pk)
    images = models.Image.objects.filter(product=product)
    context = {
        'product': product,
        'images': images
    }
    return render(request, 'product_details.html', context)

def shopping_cart(request, pk):
    cart = models.ShoppingCart.objects.get(pk=pk)
    user = cart.user
    orders = models.Order.objects.filter(cart=cart)
    tup = []
    for ord in orders:
        image = models.Image.objects.filter(product=ord.product).first
        tuplu = (ord, image)
        tup.append(tuplu)
    context = {
        'cart': cart,
        'user': user,
        'tuplu': tup
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
    except Exception:
        order = Order(cart=cart, product=product, quantity=1)
        order.save()
    else:
        check_order.quantity += 1
        check_order.save()    
    orders = models.Order.objects.filter(cart=cart)
    tup = []
    for ord in orders:
        image = models.Image.objects.filter(product=ord.product).first
        tuplu = (ord, image)
        tup.append(tuplu)
    user = cart.user
    context = {
     'cart': cart,
     'user': user,
     'tuplu': tup
    }
    return render(request, 'view_shopping_cart.html', context)


class EditProfileView(UpdateView):
    model = models.User
