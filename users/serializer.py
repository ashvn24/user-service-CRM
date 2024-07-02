from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'is_active', 'is_superuser', 'is_verified', 'is_staff', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Handle if 'password' is not in validated_data

        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
class LoginSerialisers(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    
    class Meta:
        model=CustomUser
        fields = ['id', 'email', 'is_superuser', 'password', 'access', 'refresh']
        
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        
        user = authenticate(request, email=email, password=password)
        
        if not user:
            raise ValidationError('Incorrect email or password')
        
        user_token = user.get_token()
        
        return{
            'email' : user.email,
            'is_superuser': user.is_superuser,
            'access' : str(user_token.get('access')),
            'refresh': str(user_token.get('refresh'))
        }