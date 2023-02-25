from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from drf_api.permissions import OwnerOrReadOnly
from .models import Account
from .serializers import AccountsSerializer


class AccountList(ListAPIView):
    """
    Displays a list of all the accounts and their information.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer


class AccountDetail(RetrieveUpdateAPIView):
    """
    Display account detail.
    The owner of the account can edit and delete their account here.
    """
    permission_classes = [OwnerOrReadOnly]
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
