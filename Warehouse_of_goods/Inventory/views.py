from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    clients = Client.objects.all()
    products = Product.objects.all()
    rooms = Room.objects.all()
    shelves = Shelf.objects.all()
    return render(request, 'Inventory/client_list.html', {'clients': clients, 'products': products,'rooms': rooms, 'shelves': shelves,})
