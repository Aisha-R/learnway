from rest_framework import generics
from django.contrib.auth import get_user_model
from users.serializers import CustomUserRegisterSerializer, CustomUserSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, BasePermission
from users.permissions import IsCreator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class CustomUserRegisterView(generics.CreateAPIView):
    
    model = get_user_model()
    serializer_class = CustomUserRegisterSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)

class CustomUserView(BasePermission, RetrieveAPIView):
    
    permission_classes = [IsAuthenticated, IsCreator]
    
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class CustomUserListView(LoginRequiredMixin, UserPassesTestMixin, ListAPIView):
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

    def test_func(self):
        return self.request.user.email.endswith('@admin.com')

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
