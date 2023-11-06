from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет! Это твое первое приложение!")

# Комнаты
from .models import Room

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'Inventory/room_list.html', {'rooms': rooms})

# Стеллажи
from .models import Shelf

def shelf_list(request):
    shelves = Shelf.objects.all()
    return render(request, 'Inventory/shelf_list.html', {'shelves': shelves})

# Клиенты
from .models import Client

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'Inventory/client_list.html', {'clients': clients})

# Товары
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'Inventory/product_list.html', {'products': products})