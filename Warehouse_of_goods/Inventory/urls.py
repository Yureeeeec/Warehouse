from django.urls import path
from Inventory.views import index

urlpatterns = [
    path('', index),
]


