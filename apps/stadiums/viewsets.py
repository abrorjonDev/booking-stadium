from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.stadiums.models import Stadium
from apps.stadiums.serializers import StadiumSerializer
from apps.permissions import IsOwnerOrAdmin, CanCrudStadium
from apps.user.models import RoleChoice


@extend_schema(
    request=StadiumSerializer,
    responses={200: StadiumSerializer()},
    tags=['Stadiums'])
class StadiumViewSet(ModelViewSet):
    serializer_class = StadiumSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    filterset_fields = {
        'name': ['icontains'],
        'address': ['icontains'],
        'creator': ['exact'], # for Admin only
    }

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action in {'retrieve', 'list'}:
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        else:
            self.permission_classes = [IsAuthenticated, CanCrudStadium]
        return [perm() for perm in self.permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.role == RoleChoice.OWNER:
            return Stadium.objects.filter(creator=user, deleter__isnull=True)
        return Stadium.objects.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        self.request.user.role = RoleChoice.OWNER
        self.request.user.save(update_fields=['role'])

    def perform_update(self, serializer):
        serializer.save(updater=self.request.user)

    def perform_destroy(self, instance):
        instance.deleter=self.request.user
        instance.save()
