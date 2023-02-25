from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from drf_api.permissions import OwnerOrReadOnly
from rest_framework import permissions


class CommentList(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(RetrieveUpdateDestroyAPIView):
    """
    Display comment detail, and fields where the comment can be updated
    """
    permission_classes = [OwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
