from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django_rest_passwordreset.signals import reset_password_token_created


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('email must be set')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser = True')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(max_length=50, unique = True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    context = {
        'email': reset_password_token.user.email,
        'reset_password_url': f"http://localhost:3000/password/reset/confirm/?token={reset_password_token.key}"
    }
    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = render_to_string('email/user_reset_password.txt', context)
    msg = EmailMultiAlternatives("Password Reset", email_plaintext_message, [], [reset_password_token.user.email])
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()