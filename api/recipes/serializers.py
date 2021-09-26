from rest_framework import serializers
from .models import Recipe
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email']


class RecipeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Recipe
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return Recipe.objects.create(**validated_data)