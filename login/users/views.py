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
    HTTP_500_INTERNAL_SERVER_ERROR
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
        profile = models.Profile.objects.get(user = user_id)
        name = profile.get_name()
        return Response(data={'name': name}, status=HTTP_200_OK)
    except:
        return Response({'error': 'Usuário não existe.'}, status=HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def update_profile(request):
    user_id = request.data.get('user_id')
    name = request.data.get('name')
    email = request.data.get('email')
    photo = request.data.get('photo')

    if(user_id == None or name == None or photo == None):
        return Response({'error':'Falha na requisição.'},status=HTTP_400_BAD_REQUEST)

    # verify email validation
    try:
        validate_email(email)
    except:
        return Response({'error': 'Email inválido.'}, status=HTTP_400_BAD_REQUEST)

    # Retrieve user and profile data from database
    try:
        user = models.CustomUser.objects.get(id = user_id)
        profile = models.Profile.objects.get(user = user_id)
    except:
        return Response({'error': 'Usuário não existe.'}, status=HTTP_400_BAD_REQUEST)
    
    # Set new name, email and photo
    try:
        user.set_email(email)
        profile.set_name(name)
        profile.set_photo(photo)

        user_email=user.get_email()
        profile_name = profile.get_name()
        profile_photo = profile.get_photo()
    except:
        return Response({'error': 'Erro inesperado.'}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(data={'name': profile_name, 'email': user_email, 'photo': profile_photo}, status=HTTP_200_OK)

@api_view(["POST"])
def get_profile(request):
    user_id = request.data.get('user_id')

    # Bad request if user_id is not defined
    if(user_id == None):
        return Response({'error':'Falha na requisição.'},status=HTTP_400_BAD_REQUEST)
    
    # Request user and profile according to user_id
    try:
        user = models.CustomUser.objects.get(id = user_id)
        profile = models.Profile.objects.get(user = user_id)
    except:
        return Response({'error': 'Usuário não existe.'}, status=HTTP_400_BAD_REQUEST)

    # Get email, name, photo from a certain user/profile
    try:
        user_email=user.get_email()
        profile_name = profile.get_name()
        profile_photo = profile.get_photo()
    except:
        return Response({'error': 'Erro inesperado.'}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(data={'name': profile_name, 'email': user_email, 'photo': profile_photo}, status=HTTP_200_OK)    