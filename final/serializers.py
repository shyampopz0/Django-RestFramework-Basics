from django.contrib.auth import get_user_model
from django.db.models import Q # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.core.exceptions import ValidationError
from uuid import uuid4


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(max_length=8)

    # def create(self, validated_data):
    #     user = User.objects.create(
    #         username = validated_data['username'],
    #         password = validated_data['password'],
    #         name = validated_data['name']
    #     )
    #     user.save()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'name'
        )

    def save(self):
        account = get_user_model().objects.create(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            password=self.validated_data['password'],
           # name = self.validated_data['name']
        )

        user = User.objects.create(
            username=self.validated_data['username'],
            password=self.validated_data['password'],
            name=self.validated_data['name'],
            email=self.validated_data['email']
        )

        user.save()

        password = self.validated_data['password']

        account.set_password(password)

        account.save()
        return account