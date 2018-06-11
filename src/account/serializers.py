from rest_framework import serializers

from . import models


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = models.Profile
        fields = ('url', 'read', 'wishlist', 'username')

    def get_username(self, obj):
        return obj.user.username
