from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.company.models import Company
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin





class AdminCompany(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'email', 'status', 'address')
    fieldsets = (
        (None, {'fields': ('cnpj', 'password')}),
        (('Personal info'), {'fields': ('nome', 'cnpj', 'status')}),
        (('Permissions'), {
            'fields': (
                'is_active',
            )
        }
    )),

    search_fields = ('email', 'name', 'cnpj')
    ordering = ('cnpj',)
    
    admin.site.register(Company)