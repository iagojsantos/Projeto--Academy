from django.contrib import admin
from app.accounts.models import Admin, Customer
from django.contrib.auth.admin import UserAdmin



@admin.register(Admin)
class AdminAdmin(UserAdmin):
    """Admin"""

    list_display = ("id", "email", "name")
    list_filter = ("is_active", "is_staff", "groups")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)


@admin.register(Customer)
class AdminCustomer(UserAdmin):
    """Admin"""

    list_display = ("id", "email", "name", "phone")
    list_filter = ["is_active"]
    search_fields = ("email",)
    ordering = ("email",)
    
    fieldsets = (
        (None, {"fields": ("email", "name", "password", "phone")}),
        (
            ("Permissions"),
            {"fields": ("is_active", "is_staff")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "is_staff", "name", "password1", "password2"),
            },
        ),
    )
