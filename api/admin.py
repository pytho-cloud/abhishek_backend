from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import User, Property, PropertyUser ,ContactModel ,PropertyImages


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

class PropertyImagesInline(admin.TabularInline):
    model = PropertyImages
    extra = 1


# ✅ Property admin (with image upload)



# (Optional) separate view for images
@admin.register(PropertyImages)
class PropertyImagesAdmin(admin.ModelAdmin):
    list_display = ("id", "property", "property_image")
  # how many empty forms show
# -------------------- PROPERTY ADMIN --------------------

@admin.register(Property)
class PropertyAdmin(ImportExportModelAdmin):
    inlines = [PropertyImagesInline]  

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


# @admin.register(PropertyImages)
# class PropertyImagesAdmin(admin.ModelAdmin):
#     list_display = ("id", "property", "property_image")
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



@admin.register(ContactModel)
class ContactModelAdmin(ImportExportModelAdmin):

    list_display = (
        "id",
        "templates_name",
        "phone_number",
        "email",
        "service_hrs",
        "is_active",
        # "created_at",
    )

 

    list_filter = (
        "templates_name",
    )