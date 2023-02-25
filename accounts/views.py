from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from drf_api.permissions import OwnerOrReadOnly
from .models import Account
from .serializers import AccountsSerializer


class AccountList(ListAPIView):
    """
    Displays a list of all the accounts and their information.
    Filterset_fields Can find who follows a specific user.
    The filterset_fields can also find what accounts are
    followed by a specific user.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Account.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        accounts_following_count=Count(
            'owner__account_followed', distinct=True),
        account_followed_count=Count('owner__account_followed', distinct=True)
    ).order_by('-registration_date')
    serializer_class = AccountsSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend]
    ordering_fields = [
        'posts_count',
        'accounts_following_count',
        'account_followed_count',
        ]
    search_fields = ['owner__username']
    filterset_fields = [
        'owner__account_following__account_followed__account',
        'owner__account_followed__owner__account'
        ]


class AccountDetail(RetrieveUpdateAPIView):
    """
    Display account detail.
    The owner of the account can edit and delete their account here.
    """
    permission_classes = [OwnerOrReadOnly]
    queryset = Account.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        accounts_following_count=Count(
            'owner__account_followed', distinct=True),
        account_followed_count=Count('owner__account_followed', distinct=True)
    ).order_by('-registration_date')
    serializer_class = AccountsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'posts_count',
        'accounts_following_count',
        'account_followed_count',
        ]
