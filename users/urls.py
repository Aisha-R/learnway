from django.urls import path
from users.views import CustomUserCreateView, CustomUserView, CustomUserListView

app_name = "users"

urlpatterns = [
    path('', CustomUserCreateView.as_view(), name='register'),
    path('<int:pk>/', CustomUserView.as_view(), name='read-update-delete-user'),
    path('list/', CustomUserListView.as_view(), name='users-list')
]