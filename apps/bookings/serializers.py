from rest_framework import serializers

from apps.bookings.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "date", "start_time", "end_time", "status", "stadium"]
        read_only_fields = "status",
