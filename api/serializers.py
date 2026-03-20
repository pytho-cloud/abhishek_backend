from rest_framework import serializers
from .models import Property



class PropertySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    property_name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True)
    price = serializers.DecimalField(max_digits=12, decimal_places=2)
    property_type = serializers.CharField(max_length=20)
    bhk = serializers.CharField(max_length=10, allow_blank=True)
    bedrooms = serializers.IntegerField()
    bathrooms = serializers.IntegerField()
    area_sqft = serializers.FloatField()
    address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    brochure = serializers.FileField(allow_null=True, required=False)
    status = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    # Optional: create/update methods for POST/PUT
    def create(self, validated_data):
        return Property.objects.create(**validated_data)