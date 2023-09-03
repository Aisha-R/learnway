from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authtokens.urls', namespace='authtokens')),
    path('api/users/', include('users.urls', namespace='users')),
    path('api/items/', include('items.urls', namespace='items'))
]