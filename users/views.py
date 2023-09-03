from users.serializers import CustomUserSerializer
from rest_framework import status
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.permissions import IsCreator
from items import serializers, models
    
class CustomUserCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)

class CustomUserView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsCreator]
    
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class CustomUserItemListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()
    
    def get_queryset(self):
        return models.Item.objects.filter(user=self.request.user)