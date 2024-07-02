from django.urls import path
from .views import UserRegAPIView, LoginAPIView, UserProfile

urlpatterns = [
    path('register/', UserRegAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('user/<int:id>/', UserProfile.as_view(), name='profile')
]
