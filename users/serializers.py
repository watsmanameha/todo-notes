from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', "first_name", 'last_name', 'email')


class UserSerializerFull(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', "first_name", 'last_name', 'email', 'is_staff', 'is_superuser')