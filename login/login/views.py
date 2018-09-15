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
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    try:
        user=auth.create_user_with_email_and_password(email,password)
    except:
        return Response({'error': 'Unable to create account try again'},
                            status=HTTP_400_BAD_REQUEST)
    #user = authenticate(username=username, password=password)
    session_id = user['idToken']
    return Response({'token': session_id},
                    status=HTTP_200_OK)

## Firebase

def singIn(request):
    return render(request, "signIn.html")

def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request,"signIn.html",{"msg":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)

    return render(request, "welcome.html",{"e":email})


def postsignup(request):

    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user=auth.create_user_with_email_and_password(email,passw)
        #uid = user['localId']
        #data={"name":name,"status":"1"}
        #database.child("users").child(uid).child("details").set(data)
    except:
        message="Unable to create account try again"
        return render(request,"signup.html",{"messg":message})



    return render(request,"signIn.html")

# Global variable used for the sake of simplicity.
# users = {
#     1: User(id=1, name='test', email='11@gmail.com', password='Done'),
#     2: User(id=1, name='test2', email='1ala@gmail.com', password='12345'),
# }

# class UserViewSet(viewsets.ViewSet):
#     # Required for the Browsable API renderer to have a nice form.
#     serializer_class = serializers.UserSerializer
#
#     def list(self, request):
#         serializer = serializers.UserSerializer(
#             instance=users.values(), many=True)
#         return Response(serializer.data)
