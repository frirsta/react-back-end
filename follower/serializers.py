from django.db import IntegrityError
from rest_framework import serializers
from .models import Following


class FollowingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_by = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Following
        fields = [
            'id', 'created_date', 'followed', 'owner', 'followed_by'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible dublicate'
            })
