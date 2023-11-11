from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    volume = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Полезный объем')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Помещение'
        verbose_name = 'Помещение'

class Shelf(models.Model):
    number = models.IntegerField(verbose_name='Номер')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Помещение')
    storage_capacity = models.IntegerField(verbose_name='Количество мест для хранения')
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Высота')
    width = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ширина')
    length = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Длина')
    max_load = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Максимальная нагрузка')

    def __str__(self):
        return f"Shelf {self.number}"
    
    class Meta:
        verbose_name_plural = 'Стеллажи'
        verbose_name = 'Стеллаж'

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название юридического лица')
    bank_details = models.TextField(verbose_name='Банковские реквизиты')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Клиент'
        verbose_name = 'Клиента'

class Product(models.Model):
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Высота')
    width = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ширина')
    length = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Длина')
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес')
    arrival_date = models.DateField(verbose_name='Дата поступления')
    contract_number = models.CharField(max_length=100, verbose_name='Номер договора')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    contract_end_date = models.DateField(verbose_name='Дата окончания договора')
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, verbose_name='Стеллаж')
    position = models.IntegerField(verbose_name='Позиция размещения на стеллаже')

    def __str__(self):
        return f"Product {self.id}"

    class Meta:
        verbose_name_plural = 'Товар'
        verbose_name = 'Товар'

# Create your models here.
