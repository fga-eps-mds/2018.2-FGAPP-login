import pyrebase
from django.shortcuts import render

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
    print(user)
    return render(request, "welcome.html",{"e":email})

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
