from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import SignUpSerializer, EmailSerializer, PasswordChangeSerializer


class SignUp(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer


class Email(generics.RetrieveUpdateAPIView):
    queryset = get_user_model()
    serializer_class = EmailSerializer
    def get_object(self):
        return self.request.user


class PasswordChange(generics.UpdateAPIView):
    queryset = get_user_model()
    serializer_class = PasswordChangeSerializer
    def get_object(self):
        return self.request.user