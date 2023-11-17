from django.db import models


class Brand(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Skstore/media/')
    mailFournisseur = models.EmailField()
    Num = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Skstore/media/')
    price = models.DecimalField(max_digits=5, decimal_places = 2, default=0)
    
    Brand = models.ForeignKey(Brand, null=False, on_delete=models.CASCADE, related_name="items")
    
    def __str__(self):
        return self.name


class Shop(models.Model):
    
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=255)
    items = models.ManyToManyField('Item', through='Stock')
    
    def __str__(self):
        return self.name
    

class Stock(models.Model):
    
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.shop.name} - {self.item.name} ({self.quantity} units)"