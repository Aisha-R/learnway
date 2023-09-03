from items.serializers import ItemSerializer
from items.models import Item
from rest_framework.permissions import IsAuthenticated
from items.permissions import IsCreator
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

class ItemCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        kwargs['user'] = self.request.user
        super().create(request, *args, **kwargs)
        return Response(request.data, status=status.HTTP_201_CREATED)

class ItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsCreator]
    
    serializer_class = ItemSerializer
    queryset = Item.objects.all()