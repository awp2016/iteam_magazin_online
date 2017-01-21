import datetime

from django.shortcuts import render
from django.views.generic import UpdateView
from django.views.generic.list import ListView

from iteam import forms
from iteam.models import Comment
from iteam.models import Order
from iteam.models import Product
from iteam.models import ShoppingCart
from . import models


class ProductsListView(ListView):
    model = Product
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        products = self.model.objects.all()
        context['products'] = products
        return context

    def get_queryset(self):
        return self.model.objects.order_by('-price')


def product_details(request, pk):
    form_comment = forms.CommentForm()
    product = Product.objects.get(pk=pk)
    comments = Comment.objects.filter(product=product).order_by('-date')
    context = {
        'product': product,
        'comments': comments,
        'form_comment': form_comment
    }
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(product=Product.objects.get(pk=pk),
                              text=form.cleaned_data['text'],
                              date=datetime.datetime.now(),
                              author=request.user)
            comment.save()
    return render(request, 'product_details.html', context)


def shopping_cart(request, pk):
    cart = ShoppingCart.objects.get(pk=pk)
    user = cart.user
    orders = Order.objects.filter(cart=cart)
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

    orders = Order.objects.filter(cart=cart)
    context = {
        'cart': cart,
        'user': user,
        'orders': orders
    }
    return render(request, 'view_shopping_cart.html', context)


def add_item(request, pk_cart, pk_produs):
    cart = ShoppingCart.objects.get(pk=pk_cart)
    product = Product.objects.get(pk=pk_produs)
    try:
        check_order = Order.objects.get(product=product)
    except Exception:
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
