from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.generics import (
    ListCreateAPIView, RetrieveDestroyAPIView)
from drf_api.permissions import OwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(ListCreateAPIView):
    """
    Displays a list of all the likes and their information.
    The filterset_fields can find likes made by a specific user
    The filterset_fields can also find what likes have been made
    on a specific post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.annotate(
        like_count=Count('owner__like', distinct=True),
    ).order_by('-created_date')
    serializer_class = LikeSerializer
    filter_backends = [
        DjangoFilterBackend]
    filterset_fields = [
        'post',
        'owner__like__owner__account'
        ]

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
