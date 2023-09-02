from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import CustomUser
from django.contrib.auth.password_validation import validate_password

class CustomUserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [
            UniqueValidator(
                queryset=CustomUser.objects.all()
            )
        ]
    )

    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [
            validate_password
        ],
        style = {
            "input_type": "password"
        }
    )

    confirm_password = serializers.CharField(
        write_only = True,
        required = True,
        style = {
            "input_type": "password"
        }
    )

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "password",
            "confirm_password"
        )
    
    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "password": "Passwords must match."
                }
            )
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email = validated_data["email"],
        )

        user.set_password(
            validated_data["password"]
        )

        user.save()
        
        return user
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        depth = 1

class PasswordChangeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style = {
            "input_type": "password"
        }
    )

    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        style = {
            "input_type": "password"
        }
    )

    class Meta:
        model = CustomUser
        fields = (
            'password',
            'confirm_password'
            )

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "password": "Passwords must match."
                }
            )
        return attrs

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])

        instance.save()

        return instance