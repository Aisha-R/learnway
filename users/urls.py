from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('', views.CustomUserCreateView.as_view(), name='register'),
    path('<int:pk>/', views.CustomUserView.as_view(), name='read-update-delete-user'),
    path('<int:pk>/items', views.CustomUserItemListView.as_view(), name='user-item-list')
]