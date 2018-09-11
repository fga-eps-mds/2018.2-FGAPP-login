from django.shortcuts import render
from rest_framework import generics
from accounts.serializers import AccountSerializer
from accounts.models import Account

# Create your views here.
class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
