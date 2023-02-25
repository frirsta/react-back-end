from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from drf_api.permissions import OwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(ListCreateAPIView):
    """
    Displays a list of all the comments and their information.
    The filterset_fields can find comments made by a specific user
    The filterset_fields can also find what comments have been made
    on a specific post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.annotate(
        comment_count=Count('owner__comment', distinct=True),
    ).order_by('-created_date')
    serializer_class = CommentSerializer
    filter_backends = [
        DjangoFilterBackend]
    filterset_fields = [
        'post',
        'owner__comment__owner__account'
        ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(RetrieveUpdateDestroyAPIView):
    """
    Display comment detail.
    The owner of the comment can edit and delete their comment here.
    """
    permission_classes = [OwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
