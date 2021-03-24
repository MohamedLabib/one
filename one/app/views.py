from django.shortcuts import render
# Create your views here.

def cart(request):
	return render(request, 'pages/cart.html')

def checkout(request):
	return render(request, 'pages/checkout.html')

def store(request):
	return render(request, 'pages/store.html')
