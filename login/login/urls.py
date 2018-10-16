from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from django.contrib.auth import views as auth_views
from django.contrib.sites.models import Site
from login.settings.development import LOGIN_DEFAULT_DOMAIN
from .views import status

urlpatterns = [
    path('', status),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    url(r'^api/auth-token/', obtain_jwt_token),
    url(r'^api/token-refresh/', refresh_jwt_token),
    url(r'^api/token-verify/', verify_jwt_token),
    url('^', include('django.contrib.auth.urls')),
]

try:
    site = Site.objects.get(id=1)
    site.name = LOGIN_DEFAULT_DOMAIN
    site.domain = LOGIN_DEFAULT_DOMAIN
    site.save()
    current_domain = LOGIN_DEFAULT_DOMAIN
except:
    print('please re-run the server')
