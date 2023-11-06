from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.room_list, name='room_list'),
    path('shelves/', views.shelf_list, name='shelf_list'),
    path('clients/', views.client_list, name='client_list'),
    path('products/', views.product_list, name='product_list'),
]


