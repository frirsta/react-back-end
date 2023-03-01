from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    accounts_id = serializers.ReadOnlyField(source='owner.accounts.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.accounts.profile_image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Contact
        fields = [
            'id', 'owner', 'is_owner', 'accounts_id',
            'profile_image', 'created_date', 'updated_date',
            'title', 'content'

        ]
