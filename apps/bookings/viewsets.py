from drf_spectacular.utils import extend_schema

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from apps.bookings.filters import BookingFilter
from apps.bookings.models import Booking, StatusChoice
from apps.bookings.serializers import BookingSerializer
from apps.permissions import HasObjectOwnerPermission, IsOwnerOrAdmin


@extend_schema(tags=['Bookings'])
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filterset_class = BookingFilter

    def get_permissions(self):
        if self.action in {'update', 'partial_update', 'destroy'}:
            self.permission_classes = [IsAuthenticated, HasObjectOwnerPermission]
        elif self.action in {'list', 'retrieve'}:
            self.permission_classes = [IsAuthenticated]
        elif self.action in {'cancel'}:
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

        return [perm() for perm in self.permission_classes]

    @extend_schema(
        request={},
        responses={}
    )
    @action(methods=['patch'], url_path='cancel', detail=True)
    def cancel(self, request, *args, **kwargs):
        object = self.get_object()
        object.status = StatusChoice.CANCELLED
        object.updater = request.user
        object.save()
        return Response({"detail": "Bekor qilindi."})