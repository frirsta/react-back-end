from rest_framework import serializers
from .models import Account


class AccountsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Account
        fields = ['owner', 'id', 'username', 'registration_date',
                  'updated_date', 'bio', 'profile_image']
