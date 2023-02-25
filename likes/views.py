from rest_framework import permissions
from rest_framework.generics import (
    ListCreateAPIView, RetrieveDestroyAPIView)
from drf_api.permissions import OwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(ListCreateAPIView):
    """
    Displays a list of all the Likes and their information.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(RetrieveDestroyAPIView):
    """
    Display Like detail.
    The owner of the Like can delete their Like here.
    """
    permission_classes = [OwnerOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
