from django.urls import include, path

from . import views
from .views import get_name

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('get_name/', get_name),
]