from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ReadOnlyModelViewSet

from skstore.models import Brand, Item, Stock
from skstore.serializers import BrandSerializer, ItemSerializer, StockSerializer


class ItemViewSet(ReadOnlyModelViewSet):
    
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        return Item.objects.all()
    
class BrandViewSet(ReadOnlyModelViewSet):
    
    serializer_class = BrandSerializer
    
    def get_queryset(self):
        return Brand.objects.all()
    
class StockViewSet(ReadOnlyModelViewSet):
    
    serializer_class = StockSerializer
    
    def get_queryset(self):
        return Stock.objects.all()

