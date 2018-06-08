from rest_framework import viewsets

from . import serializers
from . import models
from common import mixins


class ComicBookViewSet(mixins.RelativeURLFieldMixin, viewsets.ModelViewSet):
    serializer_class = serializers.ComicBookSerializer
    queryset = models.ComicBook.objects.all()
