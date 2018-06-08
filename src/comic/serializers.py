from rest_framework import serializers

from . import models


class ComicBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ComicBook
        fields = '__all__'
