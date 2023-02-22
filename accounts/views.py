from .models import Account
from .serializers import AccountsSerializer
from rest_framework.generics import ListAPIView


class AccountList(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
