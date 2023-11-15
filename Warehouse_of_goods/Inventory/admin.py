from django.contrib import admin
from .models import Room, Shelf, Client, Product

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'volume')

class ShelfAdmin(admin.ModelAdmin):
    list_display = ('number', 'room', 'storage_capacity', 'height', 'width', 'length', 'max_load', 'display_products')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'bank_details')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','height', 'width', 'length', 'weight', 'arrival_date', 'contract_number', 'client', 'contract_end_date', 'shelf', 'position')
    list_filter = ('client', 'shelf__room')

admin.site.register(Room, RoomAdmin)
admin.site.register(Shelf, ShelfAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)

# Register your models here.
