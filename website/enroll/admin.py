from django.contrib import admin
from .models import *
 
# Register your models here.

@admin.register(Question)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','question']


@admin.register(Result)
class UserAdmin(admin.ModelAdmin):
    list_display = ['result']


@admin.register(UserData)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user','result']
