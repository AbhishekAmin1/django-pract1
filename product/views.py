from cgitb import html
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def addProduct(request):
    print("addProduct called----")
    return HttpResponse("ADD PRODUCT")

# create view product function to display the product change

def viewproduct(request):
    return HttpResponse("viewproduct called")

#create-------

def productpage(request):
    return render(request, 'product/productpage.html')    
