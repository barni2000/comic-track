from rest_framework import viewsets

from . import serializers
from . import models
from common import mixins


class PublisherViewSet(mixins.RelativeURLFieldMixin, viewsets.ModelViewSet):
    serializer_class = serializers.PublisherSerializer
    queryset = models.Publisher.objects.all()
