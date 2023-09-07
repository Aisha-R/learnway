from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required = True
    )
    
    description= serializers.CharField(
        required = True
    )

    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )

    init_date = serializers.DateTimeField(
        read_only = True
    )

    stage = serializers.ChoiceField(
        required = False,
        choices = Item.Stage
    )

    class Meta:
        model = Item
        fields = "__all__"
        depth = 1

    def create(self, data):
        data["stage"] = Item.Stage.INITIAL
        item = Item.objects.create(**data)
        return item