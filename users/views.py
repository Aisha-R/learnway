from django.contrib.auth import get_user_model
from users.serializers import CustomUserSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsCreator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from items import serializers, models

class CustomUserItemListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()
    
    def get_queryset(self):
        return models.Item.objects.filter(user=self.request.user)
    

class CustomUserCreateView(CreateAPIView):
    
    model = get_user_model()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)
    
class CustomUserListView(LoginRequiredMixin, UserPassesTestMixin, ListAPIView):
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

    def test_func(self):
        return self.request.user.email.endswith('@admin.com')

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class CustomUserView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsCreator]
    
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer