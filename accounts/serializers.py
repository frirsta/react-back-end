from rest_framework import serializers
from .models import Account


class AccountsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Account
        fields = ['owner', 'id', 'username', 'registration_date',
                  'updated_date', 'bio', 'profile_image', 'is_owner']
