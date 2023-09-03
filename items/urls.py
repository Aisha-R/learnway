from django.urls import path
from items.views import ItemListView, ItemView, ItemCreateView

app_name = "items"

urlpatterns = [
    path('', ItemCreateView.as_view(), name='create-item'),
    path('<int:pk>/', ItemView.as_view(), name='read-update-delete-item'),
    path('list/', ItemListView.as_view(), name='items-list')
]