from django.contrib.auth import authenticate, login, logout

from rest_framework import viewsets
from rest_framework import views
from rest_framework import status
from rest_framework import permissions
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
        serializer = self.get_serializer(self.request.user.profile)

        return Response(serializer.data)


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        print(request)
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
