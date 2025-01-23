

from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import *

app_name = 'users'

urlpatterns = [    
               
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    
]
