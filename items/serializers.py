from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        depth = 1

class ItemRegisterSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required = True
    )

    description= serializers.CharField(
        write_only = True,
        required = True
    )

    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )

    class Meta:
        model = Item
        fields = (
            "title",
            "description",
            "user"
        )

    def create(self, data):
        item = Item.objects.create(**data)
        return item