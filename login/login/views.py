import pyrebase
from django.shortcuts import render
from django.contrib import auth

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

def signUp(request):

    return render(request,"signup.html")

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
