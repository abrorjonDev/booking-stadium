from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from apps.stadiums.models import Stadium
from apps.stadiums.serializers import StadiumSerializer


@extend_schema(tags=['Stadiums'])
class StadiumViewSet(ModelViewSet):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)