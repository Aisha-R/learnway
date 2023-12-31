from rest_framework import serializers, validators
from users.models import CustomUser
from django.contrib.auth.password_validation import validate_password

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [
            validators.UniqueValidator(
                queryset=CustomUser.objects.all()
            )
        ]
    )

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
        fields = "__all__"
        depth = 1

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "password": "Passwords must match."
                }
            )
        return attrs

    def update(self, user, validated_data):
        user.set_password(
            validated_data['password']
        )
        user.save()
        return user
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email = validated_data["email"],
        )
        user.set_password(
            validated_data["password"]
        )
        user.save()
        return user