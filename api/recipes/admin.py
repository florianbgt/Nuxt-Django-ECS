from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at',]