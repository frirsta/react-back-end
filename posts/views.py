from .models import Post
from .serializers import PostsSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from drf_api.permissions import OwnerOrReadOnly
from rest_framework import permissions


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    """
    Display post detail, and fields where the post can be updated
    """
    permission_classes = [OwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostsSerializer


class CreatePostView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post
    serializer_class = PostsSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
