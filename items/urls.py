from django.urls import path
from items.views import ItemListView, ItemView

app_name = "items"

urlpatterns = [
    path('', ItemListView.as_view(), name='items-list'),
    path('<int:pk>/', ItemView.as_view(), name='item')
]