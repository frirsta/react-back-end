from rest_framework import serializers
from .models import BusinessProfile
from phonenumber_field.serializerfields import PhoneNumberField


class BusinessProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.account.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.account.profile_image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = BusinessProfile
        fields = ['id', 'owner', 'is_owner', 'business_name',
                  'profile_id', 'profile_image', 'business_description',
                  'phone_number', 'registration_date', 'updated_date',
                  'business_image'
                  ]
