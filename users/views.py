from django.shortcuts import render
from rest_framework import generics, status
from . models import CustomUser
from .serializer import UserSerializer, LoginSerialisers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .producer import publish
# Create your views here.


class UserRegAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        publish('user-created', {'email': response.data['email']})
        return Response(response.data, status=status.HTTP_201_CREATED)
    
    
class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerialisers
    
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data= request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = 'id'
    queryset= CustomUser.objects.all()