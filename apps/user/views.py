from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer


class Register(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []
    authentication_classes = []

    def perform_create(self, serializer):
        serializer.save()
