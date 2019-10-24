from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response


# Create your views here.

class Upload(generics.CreateAPIView):

    def post(self, request):

        print(request.FILES['picture'])

        return Response({}, 200)


