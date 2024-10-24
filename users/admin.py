from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    ordering = ['username']  # Trier par le champ username
    list_display = ['username', 'first_name', 'last_name', 'is_staff']  # Afficher le champ username

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),  # Incluez email ici si nécessaire
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
