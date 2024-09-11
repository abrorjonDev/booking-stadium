from django.contrib.gis.geos.point import Point


from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from apps.stadiums.models import Stadium


class PointField(serializers.Field):
    def to_representation(self, value):
        return value.coords

    def to_internal_value(self, data):
        if not isinstance(data, (tuple, list)):
            raise serializers.ValidationError(_("Invalid point."))
        return Point(data)


class StadiumSerializer(serializers.Serializer):
    id  = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    address = serializers.CharField(allow_null=True, allow_blank=True, max_length=255)
    location = PointField()
    contacts = serializers.JSONField(allow_null=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return Stadium.objects.create(**validated_data)