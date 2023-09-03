from django.urls import path
from users.views import CustomUserCreateView, CustomUserView, CustomUserListView, CustomUserItemListView

app_name = "users"

urlpatterns = [
    path('', CustomUserCreateView.as_view(), name='register'),
    path('<int:pk>/', CustomUserView.as_view(), name='read-update-delete-user'),
    path('<int:pk>/items', CustomUserItemListView.as_view(), name='user-item-list'),
    path('list/', CustomUserListView.as_view(), name='users-list')
]