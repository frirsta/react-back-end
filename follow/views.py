from rest_framework import permissions
from rest_framework.generics import (
    ListCreateAPIView, RetrieveDestroyAPIView)
from drf_api.permissions import OwnerOrReadOnly
from .models import Follow
from .serializers import FollowSerializer


class FollowList(ListCreateAPIView):
    """
    Displays a list of all the Follows and their information.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowDetail(RetrieveDestroyAPIView):
    """
    Display Follow detail.
    The owner of the Follow can delete their Follow here.
    """
    permission_classes = [OwnerOrReadOnly]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
