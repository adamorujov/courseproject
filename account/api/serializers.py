from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from account.models import (
    Account, Course, Unit,
    HomeWork, Listening, ListeningQuestion, ListeningQuestionAnswer, ListeningResult,
    Reading, ReadingAnswer, ReadingResult,
    )

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

class UnitDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"

    def validate(self, attrs):
        user = self.context["request"].user
        if not user in attrs['course'].accounts.all() or not user.category == "T":
            raise ValidationError("You cannot delete a unit for this course.")

        return attrs
    

class CourseListSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True)
    units = UnitSerializer(many=True)
    class Meta:
        model = Course
        fields = ('id', 'accounts', 'name', 'units')


class CourseCreateUpdateDestroySerializer(serializers.ModelSerializer):
    accounts = serializers.SlugRelatedField(queryset=Account.objects.all(), slug_field="email", many=True)
    class Meta:
        model = Course
        fields = ('name', 'accounts')

class ListeningQuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeningQuestionAnswer
        fields = "__all__"

class ListeningQuestionSerializer(serializers.ModelSerializer):
    listeningquestionanswers = ListeningQuestionAnswerSerializer(many=True)
    class Meta:
        model = ListeningQuestion
        fields = ("listening", "question", "value", "listeningquestionanswers")


class ListeningSerializer(serializers.ModelSerializer):
    listeningquestions = ListeningQuestionSerializer(many=True)
    class Meta:
        model = Listening
        fields = ("homework", "name", "audio", "max_result", "listeningquestions")

class ReadingAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingAnswer
        fields = "__all__"

class ReadingSerializer(serializers.ModelSerializer):
    readinganswers = ReadingAnswerSerializer(many=True)
    class Meta:
        model = Reading
        fields = ("homework", "name", "text", "max_result", "readinganswers")

class HomeWorkSerializer(serializers.ModelSerializer):
    listenings = ListeningSerializer(many=True)
    readings = ReadingSerializer(many=True)
    class Meta:
        model = HomeWork
        fields = ("course", "name", "listenings", "readings")

