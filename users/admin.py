from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'full_name',
        'email',
        'phone',
        'age',
        'is_active',
        'created_at'
    ]

    search_fields = [
        'full_name',
        'email',
        'phone'
    ]

    list_filter = [
        'is_active',
        'age',
        'created_at'
    ]

    ordering = ['full_name']
