from rest_framework import serializers
from .models import Post


class PostsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    accounts_id = serializers.ReadOnlyField(source='owner.accounts.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.accounts.profile_image.url')

    def validate_post_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.post_image.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px!')
        if value.post_image.height > 4096:
            raise serializers.ValidationError('Image height larger than 4096px!')
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'owner', 'created_date', 'updated_date',
            'caption', 'image', 'profile_image',
            'is_owner', 'accounts_id', 'id'
        ]
