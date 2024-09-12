from rest_framework.viewsets import ModelViewSet

from apps.bookings.models import Booking
from apps.bookings.serializers import BookingSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filterset_class =