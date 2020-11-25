from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserAccountGet

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username']
        )

        user.save()

    class Meta:
        model = User
        fields = ['username','email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = User.objects.create_user(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
           # name = self.validated_data['name']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password!=password2:
            raise serializers.ValidationError({'password':'passwords must match'})
        account.set_password(password)
        account.save()
        return account