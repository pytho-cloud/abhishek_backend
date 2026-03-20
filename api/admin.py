from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import User, Property, PropertyUser


# -------------------- USER ADMIN --------------------

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):

    list_display = (
        "id",
        "username",
        "email",
        "phone",
        "created_at",
    )

    search_fields = (
        "username",
        "email",
        "phone",
    )

    list_filter = (
        "created_at",
    )


# -------------------- PROPERTY ADMIN --------------------

@admin.register(Property)
class PropertyAdmin(ImportExportModelAdmin):

    list_display = (
        "id",
        "property_name",
        "property_type",
        "price",
        "status",
        "created_at",
    )

    search_fields = (
        "property_name",
        "city",
        "state",
    )

    list_filter = (
        "property_type",
        "status",
        "created_at",
    )


# -------------------- PROPERTY USER ADMIN --------------------

@admin.register(PropertyUser)
class PropertyUserAdmin(ImportExportModelAdmin):

    list_display = (
        "id",
        "username",
        "phone",
        "email",
        "user_click_location",
        "user_property_location",
        "created_at",
    )

    search_fields = (
        "username",
        "user_click_location",
    )

    list_filter = (
        "created_at",
    )