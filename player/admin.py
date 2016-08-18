from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from player.models import Player
# Register your models here.
admin.site.register(Player)