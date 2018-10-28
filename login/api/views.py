from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework import status
from django.conf import settings
import requests
from users.models import Profile
from users.models import CustomUser

@api_view(["POST"])
def registration(request):
    email = request.data.get('email')
    password1 = request.data.get('password1')
    password2 = request.data.get('password2')
    request_json = {"email": email, "password1": password1, "password2": password2}
    try:
        response = requests.post(settings.LOGIN_DEFAULT_DOMAIN + '/api/rest-auth/registration/', json=request_json)
        response_json = response.json()
        #Criação do perfil assim que o usuário é registrado
        if 'user' in response_json:
            if 'pk' in response_json['user']:
                user_id=response_json['user']['pk']
                user = CustomUser.objects.get(pk = user_id)
                profile = Profile(user=user, name='', photo='')
                profile.save()

        return Response(data=response_json, status=response.status_code)

    except:
        return Response({'error': 'Erro interno de servidor'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)
