import pyrebase
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

config = {
    'apiKey': "AIzaSyDl2wMlfPQ3ZqmUgfb7ry_KeJBcE36GgKc",
    'authDomain': "fgapp-c3fec.firebaseapp.com",
    'databaseURL': "https://fgapp-c3fec.firebaseio.com",
    'projectId': "fgapp-c3fec",
    'storageBucket': "fgapp-c3fec.appspot.com",
    'messagingSenderId': "350137456383"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

## Django rest auth

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))

def signUp(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if email is None or password is None:
        return Response({'error': 'Os campos não podem estar vazios'},
                        status=HTTP_400_BAD_REQUEST)
    if len(password)<6 or len(password)>15:
        return Response({'error': 'A senha deve conter de 6 a 15 caracteres'},
            status=HTTP_400_BAD_REQUEST)
    try:
        user=auth.create_user_with_email_and_password(email,password)
    except:
        return Response({'error': 'Unable to create account try again'},
                            status=HTTP_404_NOT_FOUND)
    #user = authenticate(username=username, password=password)
    session_id = user['idToken']
    return Response({'token': session_id},
                    status=HTTP_200_OK)
