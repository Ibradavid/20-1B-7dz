from rest_framework import serializers
from .models import CustomUser, Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'age', 'password', 'created_at']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'description', 'is_completed', 'created_at', 'image']
        read_only_fields = ['user', 'created_at']
