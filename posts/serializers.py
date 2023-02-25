from rest_framework import serializers
from .models import Post
from likes.models import Like


class PostsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    accounts_id = serializers.ReadOnlyField(source='owner.accounts.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.accounts.profile_image.url')
    likes_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_post_image(self, value):
        """
        Throws error if the image width or height is larger than 4096px
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!')
        if value.post_image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!')
        if value.post_image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!')
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_likes_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            likes = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return likes.id if likes else None
            print(likes)
        return None

    class Meta:
        model = Post
        fields = [
            'owner', 'created_date', 'updated_date',
            'caption', 'post_image', 'profile_image',
            'is_owner', 'accounts_id', 'id',
            'likes_id', 'likes_count', 'comments_count'
        ]
