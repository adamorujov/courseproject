from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from account.models import Account, Course, Unit

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "first_name", "last_name", "email", "category", "is_staff", "date_joined", "last_login")

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "email", "category", "password")

    def validate(self, data):
        validate_password(data["password"])
        return data

    def create(self, validated_data):
        account = Account.objects.create(
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            email = validated_data["email"],
            category = validated_data["category"]
        )
        account.set_password(validated_data["password"])
        account.save()
        return account

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"

class UnitCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"

    def validate(self, attrs):
        user = self.context["request"].user
        if not user in attrs['course'].accounts.all() or not user.category == "T":
            raise ValidationError("You cannot create a unit for this course.")

        return attrs

class CourseListSerializer(serializers.ModelSerializer):
    accounts = serializers.SerializerMethodField()
    units = UnitSerializer(many=True)
    class Meta:
        model = Course
        fields = ('accounts', 'name', 'units')

    def get_accounts(self, obj):
        return AccountSerializer(obj.accounts.all(), many=True).data

class CourseCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"



