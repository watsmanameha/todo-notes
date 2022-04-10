from rest_framework import viewsets, mixins

from .models import User
from .serializers import UserModelSerializer
from rest_framework.permissions import IsAdminUser


class UserModelViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
