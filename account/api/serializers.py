from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password
from account.models import Account

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ("first_name", "last_name", "email", "category")

class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "email", "category", "password")

    def validate(self, data):
        validate_password(data["password"])
        return data

    def create(self, validated_data):
        account = Account.objects.create(
            email = validated_data["email"],
        )
        account.set_password(validated_data["password"])
        account.save()
        return account
