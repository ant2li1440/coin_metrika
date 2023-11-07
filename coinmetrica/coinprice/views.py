from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


from .models import *
menu = [{'title': 'Title', 'url_name': 'home'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'addpage', 'url_name': 'addpage'},
        {'title': 'login', 'url_name': 'login'}]
def index(request):
    posts = coins.objects.all()
    context = {'posts': posts,
               'menu': menu,
               'title':'Title'
    }
    return render(request, 'coinprice/index.html', context=context)

def about(request):
    return render(request, 'coinprice/about.html', {'menu': menu, 'title': 'About'})
def price(request, priceid):
    print(request.GET)
    return HttpResponse(f"<h1>Price</h1><p>{priceid}</p>")

def addpage(request):
    return HttpResponse('addpage')

def login(request):
    return HttpResponse('login')

def pageNotFound(request, exception):
    return HttpResponseNotFound("error")

def show_price(request, post_id):
    return HttpResponse('coin N = {post_id}')
