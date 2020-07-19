from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

from core import models as core_models


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name')
        user.last_name = self.validated_data.get('last_name')
        user.save(update_fields=['first_name', 'last_name'])


class UserProfile(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = core_models.UserProfile
        # exclude = ('password', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser')


class CustomUserDetailsSerializer(UserDetailsSerializer):
    profile = UserProfile(source='userprofile', read_only=True, required=False)

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('profile',)
        # read_only_fields = ('profile',)
