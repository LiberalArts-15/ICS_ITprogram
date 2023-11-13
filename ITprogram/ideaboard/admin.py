from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {
            "fields": ("profile_pic", "intro"),
        }),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Post)