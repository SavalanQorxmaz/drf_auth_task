
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    
]
