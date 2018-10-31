from django.urls import include, path
from django.views.generic import TemplateView
from django.conf.urls import url

from .views import RegisterView, VerifyEmailView

urlpatterns = [
    path('users/', include('users.urls')),
    path('', include('rest_auth.urls')),
    url(r'^registration/$', RegisterView.as_view(), name='rest_register'),
    url(r'^registration/verify-email/$', VerifyEmailView.as_view(), name='rest_verify_email'),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
        name='account_confirm_email'),

]
