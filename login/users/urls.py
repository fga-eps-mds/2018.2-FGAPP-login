from django.urls import include, path

from . import views
from .views import get_name, set_name, update_email

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('get_name/', get_name),
    path('set_name/', set_name),
    path('update_email/', update_email),
]
