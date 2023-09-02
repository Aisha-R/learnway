from rest_framework.generics import ListAPIView, RetrieveAPIView
from items.serializers import ItemSerializer, ItemRegisterSerializer
from items.models import Item
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.permissions import IsAuthenticated, BasePermission
from items.permissions import IsCreator
from rest_framework import generics
from rest_framework import permissions, status
from rest_framework.response import Response

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

class ItemRegisterView(generics.CreateAPIView):
    
    model = Item
    serializer_class = ItemRegisterSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        kwargs['user'] = self.request.user
        super().create(request, *args, **kwargs)
        return Response(request.data, status=status.HTTP_201_CREATED)