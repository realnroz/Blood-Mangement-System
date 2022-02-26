from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import User
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display        = ('email','date_joined','last_login','is_admin')
    list_filter         = ()
    readonly_fields     = ('date_joined','last_login')
    fieldsets = (
        ('User Info', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin','is_staff','is_superuser','is_active')}),
    )

    search_fields = ('email',)
    ordering= ('email',)
    filter_horizontal = ()
