from rest_framework.generics import ListAPIView, RetrieveAPIView
from items.serializers import ItemSerializer
from items.models import Item
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.permissions import IsAuthenticated, BasePermission
from items.permissions import IsCreator

class ItemListView(LoginRequiredMixin, UserPassesTestMixin, ListAPIView):
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

    def test_func(self):
        return self.request.user.email.endswith('@admin.com')

    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class ItemView(BasePermission, RetrieveAPIView):
    
    permission_classes = [IsAuthenticated, IsCreator]
    
    serializer_class = ItemSerializer
    queryset = Item.objects.all()