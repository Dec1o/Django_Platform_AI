from django.contrib import admin
from .models import GroupFile

@admin.register(GroupFile)
class GroupFileAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'company')
