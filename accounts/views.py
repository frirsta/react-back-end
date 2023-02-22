from .models import Account
from .serializers import AccountsSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from drf_api.permissions import OwnerOrReadOnly


class AccountList(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer


class AccountDetail(RetrieveAPIView):
    """
    Display profile detail, and fields where the profile can be updated
    """
    permission_classes = [OwnerOrReadOnly]
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
