from .models import Post
from .serializers import PostsSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from drf_api.permissions import OwnerOrReadOnly


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
