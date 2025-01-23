
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),  # DRF-nin daxili autentifikasiyası
    path("api/auth/google/", GoogleLogin.as_view(), name="google_login"),            # Google OAuth2 üçün
    path("auth/", include("users.urls")), 
    
]
