from django.db.models import Count
from rest_framework import permissions, filters
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
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comment_count=Count('comment', distinct=True)
    ).order_by('-created_date')
    serializer_class = PostsSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = [
        'likes_count',
        'comment_count',
        ]
    search_fields = [
        'owner__username',
        'caption',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(RetrieveUpdateDestroyAPIView):
    """
    Display post detail.
    The owner of the post can edit and delete their post here.
    """
    permission_classes = [OwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comment_count=Count('comment', distinct=True)
    ).order_by('-created_date')
    serializer_class = PostsSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = [
        'likes_count',
        'comment_count',
        ]
    search_fields = [
        'owner__username',
        'caption',
    ]
