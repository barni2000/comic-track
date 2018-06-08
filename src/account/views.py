from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from . import models
from common import mixins


class ProfileViewSet(mixins.RelativeURLFieldMixin, viewsets.ModelViewSet):
    serializer_class = serializers.ProfileSerializer
    queryset = models.Profile.objects.all()

    @action(detail=False)
    def me(self, request):
        profile = self.queryset[0]
        serializer = self.get_serializer(profile)

        return Response(serializer.data)
