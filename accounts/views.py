from .models import Account
from .serializers import AccountsSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


class AccountList(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer


class AccountDetail(RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
