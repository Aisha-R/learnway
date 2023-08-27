from django.shortcuts import render
from rest_framework.generics import ListAPIView
from items.serializers import ItemSerializer
from items.models import Item

class ItemListView(ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()