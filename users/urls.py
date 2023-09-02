from django.urls import path
from users.views import CustomUserRegisterView, CustomUserView, CustomUserListView, CustomUserDeleteView

app_name = "users"

urlpatterns = [
    path('', CustomUserListView.as_view(), name='users-list'),
    path('register/', CustomUserRegisterView.as_view(), name='register'),
    path('<int:pk>/', CustomUserView.as_view(), name='read'),
    path('<int:pk>/delete/', CustomUserDeleteView.as_view(), name='item')
]