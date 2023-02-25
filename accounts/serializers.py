from rest_framework import serializers
from .models import Account
from follow.models import Follow


class AccountsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    accounts_following_id = serializers.SerializerMethodField()
    accounts_following_count = serializers.ReadOnlyField()
    account_followed_count = serializers.ReadOnlyField()
    posts_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_accounts_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            accounts_following = Follow.objects.filter(
                owner=user, account_followed=obj.owner
            ).first()
            return accounts_following.id if accounts_following else None
        return None

    class Meta:
        model = Account
        fields = ['owner', 'id', 'registration_date',
                  'updated_date', 'bio', 'profile_image', 'is_owner',
                  'posts_count', 'account_followed_count',
                  'accounts_following_count', 'accounts_following_id'
                  ]
