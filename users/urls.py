from django.urls import path
from users.views import CustomUserRegisterView, CustomUserReadView

app_name = "users"

urlpatterns = [
    path('register/', CustomUserRegisterView.as_view(), name='register'),
    path('<int:pk>/', CustomUserReadView.as_view(), name='read')
]