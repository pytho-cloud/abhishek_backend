from django.db import models

# Create your models here.



class User(models.Model):
    username = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # when created
    updated_at = models.DateTimeField(auto_now=True)      # when updated
    def __str__(self):
        return self.username if self.username else self.email

    class Meta:
        ordering = ["-created_at"]   # newest first
        verbose_name = "User"
        verbose_name_plural = "Users"




from django.db import models


class Property(models.Model):

    PROPERTY_TYPE_CHOICES = (
        ("house", "House"),
        ("residential", "Residential"),
        ("villa", "Villa"),
        ("land", "Land"),
        ("commercial", "Commercial"),
      

    )

    BHK_CHOICES = (
        ("1RK", "1 RK"),
        ("1BHK", "1 BHK"),
        ("2BHK", "2 BHK"),
        ("3BHK", "3 BHK"),
        ("4BHK", "4 BHK"),
        ("5BHK+", "5 BHK+"),
    )



    STATUS_CHOICES = (
        ("available", "Available"),
        ("sold", "Sold"),
        ("rented", "Rented"),
        ("undevelopment", "Undevelopment"),
        ("near", "Nearest Possessions"),
        ("ready", "Ready To Move"),
    )

    # Basic Info
    property_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # Pricing
    price = models.DecimalField(max_digits=12, decimal_places=2)

    # Property Details
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    bhk = models.CharField(max_length=20,null=True,blank=True)



    brochure = models.FileField(upload_to="brochures/", blank=True, null=True)

    # Location
    pincode = models.CharField(max_length=255)
    address = models.TextField(max_length=100)
    location = models.TextField(max_length=100)

    # state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    # Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")


    # Dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.property_name

    class Meta:
        ordering = ["-created_at"]


class PropertyImages(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="images"
    )
    property_image = models.ImageField(upload_to="properties/" ,null=True,blank=True)


class PropertyUser(models.Model):
    username = models.CharField(max_length=150, blank=True)

    user_click_location = models.CharField(
        max_length=255,
        blank=True,
        help_text="Location user clicked on"
    )

    user_property_location = models.CharField(
        max_length=255,
        blank=True,
        help_text="Property location viewed by user"
    )
    phone = models.CharField(max_length=255,null=True,blank=True)
    email = models.CharField(max_length=255,null=True)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    is_search = models.BooleanField(default=False, null=True ,blank=True)
    is_click = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.username if self.username else "Anonymous User"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Property User Activity"
        verbose_name_plural = "Property User Activities"



class ContactModel(models.Model):
    templates_name  = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255,null=True)
    description = models.TextField()
    email = models.CharField(max_length=255,null=True)
    service_hrs = models.CharField(max_length=255,null=True)
    is_active = models.BooleanField(default=False)



    def __str__(self):
        return self.templates_name
    







class Blog:
    pass