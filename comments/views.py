from rest_framework import permissions
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from drf_api.permissions import OwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(ListCreateAPIView):
    """
    Displays a list of all the comments and their information.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

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
