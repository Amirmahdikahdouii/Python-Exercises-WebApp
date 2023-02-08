from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from Accounts.views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jwt-auth/token/', CustomTokenObtainPairView.as_view()),
    path('jwt-auth/token/refresh/', TokenRefreshView.as_view()),
    path('jwt-auth/token/verify/', TokenVerifyView.as_view()),
    path('api/', include('questions.urls', namespace='questions')),
    path("api/", include("Accounts.urls")),
    path("rest-auth/", include('dj_rest_auth.urls')),
    path("rest-auth/register/", include('dj_rest_auth.registration.urls')),
]
