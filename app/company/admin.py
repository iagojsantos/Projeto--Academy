from django.contrib import admin
from app.company.models import Company





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