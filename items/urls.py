from django.urls import path
from items.views import ItemListView

app_name = "items"

urlpatterns = [
    path('', ItemListView.as_view(), name='items-list')
]