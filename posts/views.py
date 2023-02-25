from rest_framework import permissions
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from drf_api.permissions import OwnerOrReadOnly
from .models import Post
from .serializers import PostsSerializer


class PostList(ListCreateAPIView):
    """
    Displays a list of all the posts and their information.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(RetrieveUpdateDestroyAPIView):
    """
    Display post detail.
    The owner of the post can edit and delete their post here.
    """
    permission_classes = [OwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
