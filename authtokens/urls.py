from django.urls import path 
from rest_framework_simplejwt import views

app_name = "authtokens"

urlpatterns = [
    path('', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.TokenBlacklistView.as_view(), name='token_blacklist')
]