from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from . import user
from .user import User
from . import serializers
import pyrebase

config = {
  "apiKey": "AIzaSyDGYMhqucbTLekTaBFumSKbMtX7zLrDNUY",
  "authDomain": "fgapplogin.firebaseapp.com",
  "databaseURL": "https://fgapplogin.firebaseio.com",
  "projectId": "fgapplogin",
  "storageBucket": "fgapplogin.appspot.com",
  "messagingSenderId": "106726536163"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# Global variable used for the sake of simplicity.
users = {
    1: User(id=1, name='test', email='11@gmail.com', password='Done'),
    2: User(id=1, name='test2', email='1ala@gmail.com', password='12345'),
}

class UserViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.UserSerializer

    def list(self, request):
        serializer = serializers.UserSerializer(
            instance=users.values(), many=True)
        return Response(serializer.data)