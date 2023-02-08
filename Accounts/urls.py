from django.urls import path
from . import views

urlpatterns = [
    path("", views.CustomTokenObtainPairView.as_view()),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path("check-username/", views.CheckUsernameView.as_view(), name="check_username")
]
