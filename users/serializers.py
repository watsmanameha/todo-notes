from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import User


class UserModelSerializer(ModelSerializer):
    # id = PrimaryKeyRelatedField(
    #     queryset=User.objects.all(),
    #     allow_null=True,
    #     default=None
    # )

    # def validate_user(self, value):
    #     return self.context['request'].user

    class Meta:
        model = User
        fields = ["id", "username", "firstname", "lastname", "email"]
