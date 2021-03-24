from django.shortcuts import render
from .models import Persons
# Create your views here.

def home(request):
	names = Persons.objects.all()
	return render(request, 'pages/home.html', {'names':names})

def cart(request):
	return render(request, 'pages/cart.html')

def checkout(request):
	return render(request, 'pages/checkout.html')

def store(request):
	return render(request, 'pages/store.html')
