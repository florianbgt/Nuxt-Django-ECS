from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth import get_user_model
from .models import Recipe
from .serializers import RecipeSerializer


class OwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or obj.user == request.user:
            return True


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, OwnerOrReadOnly]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer