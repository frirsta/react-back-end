from django.db import IntegrityError
from rest_framework import serializers
from .models import Follow


class FollowSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    account_followed_name = serializers.ReadOnlyField(source='account_followed.username')

    class Meta:
        model = Follow
        fields = [
            'id', 'created_date', 'account_followed', 'owner',
            'account_followed_name'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible dublicate'
            })
