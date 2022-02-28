from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def group(request):
    return HttpResponse("Group called---")

def contactUs(request):
    return render(request, 'group/contactUs.html')

def index(request):
    return render(request, 'group/index.html')