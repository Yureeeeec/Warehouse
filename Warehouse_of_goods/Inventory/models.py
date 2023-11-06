from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Shelf(models.Model):
    number = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    storage_capacity = models.IntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    max_load = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Shelf {self.number}"

class Client(models.Model):
    name = models.CharField(max_length=100)
    bank_details = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    height = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    arrival_date = models.DateField()
    contract_number = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    contract_end_date = models.DateField()
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    position = models.IntegerField()

    def __str__(self):
        return f"Product {self.id}"


# Create your models here.
