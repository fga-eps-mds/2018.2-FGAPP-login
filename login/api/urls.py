from django.urls import include, path
from .views import registration
from .views import login
#from .views import logout
urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('registration/', registration),
    path('login/', login),
    #path('logout/', logout),

]
