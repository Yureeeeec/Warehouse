from django.contrib import admin
from .models import Room, Shelf, Client, Product

admin.site.register(Room)
admin.site.register(Shelf)
admin.site.register(Client)
admin.site.register(Product)

# Register your models here.
