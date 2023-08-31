from rest_framework import generics
from django.contrib.auth import get_user_model
from users.serializers import CustomUserRegisterSerializer, CustomUserReadSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, BasePermission
from users.permissions import IsCreator

class CustomUserRegisterView(generics.CreateAPIView):
    
    model = get_user_model()
    serializer_class = CustomUserRegisterSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)

class CustomUserReadView(BasePermission, RetrieveAPIView):
    
    permission_classes = [IsAuthenticated, IsCreator]
    
    serializer_class = CustomUserReadSerializer
    queryset = CustomUser.objects.all()
