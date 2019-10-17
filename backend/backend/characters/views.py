from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Character
from .serializers import CharacterSerializer


class CharacterList(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = ()


class CharacterDestroy(generics.DestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class CharacterUpdate(generics.UpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class CharacterCreate(generics.CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )


class CharacterGet(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = ()

