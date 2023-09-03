from django.urls import path
from items import views

app_name = "items"

urlpatterns = [
    path('', views.ItemCreateView.as_view(), name='create-item'),
    path('<int:pk>/', views.ItemView.as_view(), name='read-update-delete-item')
]