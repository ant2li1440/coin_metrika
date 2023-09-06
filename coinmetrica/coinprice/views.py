from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("qqq")

def price(request, priceid):
    print(request.GET)
    return HttpResponse(f"<h1>Price</h1><p>{priceid}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("error")
