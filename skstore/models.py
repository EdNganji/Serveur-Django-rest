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
    
    Brand = models.ForeignKey(Brand, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    