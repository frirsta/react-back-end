from rest_framework import serializers
from .models import BusinessProfile
from django.contrib.auth.models import User
from phonenumber_field.serializerfields import PhoneNumberField


class BusinessProfileSerializer(serializers.ModelSerializer):
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
        fields = ['id', 'owner', 'is_owner', 'accounts_following_id',
                  'accounts_following_count', 'account_followed_count',
                  'posts_count', 'business_name', 'business_description',
                  'phone_number', 'registration_date', 'updated_date',
                  'business_image'
                  ]
