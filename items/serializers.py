from rest_framework import serializers
from .models import Item

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        depth = 1

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        depth = 1