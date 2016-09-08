from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from player.models import Profile
# Register your models here.
admin.site.register(Profile)