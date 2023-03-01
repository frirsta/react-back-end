from django.db.models import Count
from rest_framework import permissions, filters
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from drf_api.permissions import OwnerOrReadOnly
from .models import BusinessProfile
from .serializers import BusinessProfileSerializer


class BusinessProfileList(ListAPIView):
    """
    Displays a list of all the Business Profiles and their information.
    Filterset_fields Can find who follows a specific user.
    The filterset_fields can also find what Business Profiles are
    followed by a specific user.
    """
    serializer_class = BusinessProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = BusinessProfile.objects.all()
    filter_backends = [
        filters.SearchFilter,
        ]
    search_fields = ['owner__username']


class BusinessProfileDetail(RetrieveUpdateAPIView):
    """
    Display account detail.
    The owner of the account can edit and delete their account here.
    """
    permission_classes = [OwnerOrReadOnly]
    serializer_class = BusinessProfileSerializer
    queryset = BusinessProfile.objects.all()
