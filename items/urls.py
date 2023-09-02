from django.urls import path
from items.views import ItemListView, ItemView, ItemRegisterView

app_name = "items"

urlpatterns = [
    path('create/', ItemRegisterView.as_view(), name='create-item'),
    path('', ItemListView.as_view(), name='items-list'),
    path('<int:pk>/', ItemView.as_view(), name='item')
]