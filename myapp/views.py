from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def menu(request):
    return render(request, 'menu.html')
def cart(request):
    return render(request, 'cart.html')