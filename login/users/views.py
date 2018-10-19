from rest_framework import generics
from . import models
from . import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)

import requests
from django.core.validators import validate_email

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class ProfileListView(generics.ListCreateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

@api_view(["POST"])
def get_name(request):
    user_id = request.data.get('user_id')
    if(user_id == None):
        return Response({'error':'Falha na requisição.'},status=HTTP_400_BAD_REQUEST)

    try:
        user = models.CustomUser.objects.get(id = user_id)
        name = user.get_full_name()
        return Response(data={'name': name}, status=HTTP_200_OK)
    except:
        return Response({'error': 'Usuário não existe.'}, status=HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def set_name(request):
    first_name = request.data.get('first_name')
    user_id = request.data.get('user_id')
    if(user_id == None):
        return Response({'error':'Falha na requisição.'},status=HTTP_400_BAD_REQUEST)

    try:
        user = models.CustomUser.objects.get(id = user_id)
        user.set_full_name(first_name)
        user_name = user.get_full_name()
        return Response(data={'name': user_name} , status=HTTP_200_OK)
    except:
        return Response({'error': 'Usuário não existe.'}, status=HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def update_email(request):
    email = request.data.get('email')
    user_id = request.data.get('user_id')

    try:
        validate_email(email)
    except:
        return Response({'error': 'Email inválido.'}, status=HTTP_400_BAD_REQUEST)

    if(user_id == None):
        return Response({'error':'Falha na requisição.'}, status=HTTP_400_BAD_REQUEST)

    try:
        user = models.CustomUser.objects.get(id = user_id)
        user.set_email(email)
        user_email=user.get_email()
        return Response(data={'email': email}, status=HTTP_200_OK)
    except:
        return Response({'error': 'Usuário não existe.'}, status=HTTP_400_BAD_REQUEST)
