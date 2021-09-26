from django.db import models
from django.contrib.auth import get_user_model


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='recipes/%Y/%m/%d')
    instruction = models.TextField(max_length=10000)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name