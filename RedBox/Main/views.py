from django.shortcuts import render, get_object_or_404,render_to_response
from django.template import RequestContext
from .models import Category,Product
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from cart.forms import CartAddProductForm
from .forms import Sort

# Create your views here.
def index(request):
    Movies = Product.objects.filter(category__name = 'Movies')
    Games = Product.objects.filter(category__name = 'Games')
    form = Sort()
    context = {
    'movies': Movies,
    'games': Games,
    'form': form
    }

    return render(request,'product/index.html', context)


def movie_detail(request,id):
    movie = get_object_or_404(Product, id= id)
    cart_product_form = CartAddProductForm()
    context = {
        'title': movie.name,
        'movie': movie,
        'cart_product_form': cart_product_form
    }
    return render(request, 'product/detail.html', context)


def game_detail(request,id):
    game = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    context = {
        'title': game.name,
        'game': game,
        'cart_product_form': cart_product_form
    }
    return render(request, 'product/detail.html', context)

