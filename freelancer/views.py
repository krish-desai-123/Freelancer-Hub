from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import *


class ClientListView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = {
        'GET': ClientListSerializer,
        'POST': ClientCreateSerializer,
    }
    def get_queryset(self):
        return Client.objects.select_related('user').all().order_by('-created_at')

    def get_serializer_class(self):
        return self.serializer_class.get(self.request.method)