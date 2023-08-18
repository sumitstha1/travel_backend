from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            "uid",
            "name",
            "slug"
        ]
        model = Country

class CitySerializer(serializers.ModelSerializer):

    country = CountrySerializer(read_only = True)

    class Meta:
        fields = [
            "uid",
            "country",
            "name",
            "slug"
        ]
        model = City

class DestinationImageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            "uid",
            "imgSrc"
        ]
        model = DestinationImage

class DestinationSerializer(serializers.ModelSerializer):

    location = CountrySerializer(read_only = True)
    city = CitySerializer(read_only = True)
    imgSrc = DestinationImageSerializer(read_only = True, many = True)

    class Meta:
        fields = [
            "uid",
            "created_at",
            "updated_at",
            "title",
            "location",
            "city",
            "grade",
            "fees",
            "meta_desc",
            "description",
            "slug",
            "imgSrc"
        ]
        model = Destination