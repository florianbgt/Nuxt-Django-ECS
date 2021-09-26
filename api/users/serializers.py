from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=get_user_model().objects.all())])
    password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'password2',)

    def validate(self, value):
        if value['password'] != value['password2']:
            raise serializers.ValidationError({"password2": "Password fields did not match"})
        return value

    def create(self, validated_data):
        user = get_user_model().objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        depth = 1
        fields = ('id', 'email',)


class PasswordChangeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ('old_password', 'password', 'password2')

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({'old_password': 'Old password is incorrect'})
        return value

    def validate(seld, value):
        if value['password'] != value['password2']:
            raise serializers.ValidationError({'password2': 'Password fields did not match'})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        return instance