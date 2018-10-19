from django.urls import include, path

from . import views
from .views import get_name, update_profile, get_profile

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('profiles/', views.ProfileListView.as_view()),
    path('get_name/', get_name),
    path('update_profile/', update_profile),
    path('get_profile/', get_profile),
]
