from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    account_id = serializers.ReadOnlyField(source='account.id')
    profile_image = serializers.ReadOnlyField(
        source='account.profile_image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'account_id', 'profile_image')
