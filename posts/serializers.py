from rest_framework import serializers
from .models import Post


class PostsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    accounts_id = serializers.ReadOnlyField(source='owner.accounts.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.accounts.profile_image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'owner', 'created_date', 'updated_date',
            'caption', 'post_image', 'profile_image',
            'is_owner', 'accounts_id'
        ]
