from django.conf.urls import url
from accounts import views
from django.conf.urls import include

urlpatterns = [
    url(r'^accounts/$', views.AccountList.as_view()),
    url(r'^accounts/(?P<pk>[0-9]+)/$', views.AccountDetail.as_view()),

    url(r'^api-auth/', include('rest_framework.urls')),
]
