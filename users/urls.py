from django.urls import path
from .views import UserRegAPIView, LoginAPIView

urlpatterns = [
    path('register/', UserRegAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login')
]
