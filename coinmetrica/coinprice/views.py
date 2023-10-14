from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


from .models import *
menu = ['Title', 'About']
def index(request):
    posts = coins.objects.all()
    return render(request, 'coinprice/index.html', {'posts': posts, 'menu': menu, 'title':'Title'})

def about(request):
    return render(request, 'coinprice/about.html', {'menu': menu, 'title': 'About'})
def price(request, priceid):
    print(request.GET)
    return HttpResponse(f"<h1>Price</h1><p>{priceid}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("error")
