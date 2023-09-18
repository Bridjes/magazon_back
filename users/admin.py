from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'get_groups')

    def get_groups(self, obj):
        return ", ".join([str(group) for group in obj.groups.all()])

    get_groups.short_description = 'Groups'