from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, UserSerializerFull
from .models import User


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserSerializerFull
        return UserSerializer
