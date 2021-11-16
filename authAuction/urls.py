from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
urlpatterns = [
path('login/', TokenObtainPairView.as_view()),
path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
path('refresh/', TokenRefreshView.as_view()),
path('verifyToken/', views.VerifyTokenView.as_view()),
path('user', views.UserCreateView.as_view()),
path('user/<int:pk>', views.UserDetailView.as_view()),
]
