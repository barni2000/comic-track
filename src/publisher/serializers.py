from rest_framework import serializers

from . import models


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Publisher
        fields = '__all__'
