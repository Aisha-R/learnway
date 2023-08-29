from rest_framework.generics import ListAPIView
from items.serializers import ItemSerializer
from items.models import Item
from django.contrib.auth.mixins import LoginRequiredMixin

class ItemListView(LoginRequiredMixin, ListAPIView):
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

    serializer_class = ItemSerializer
    queryset = Item.objects.all()