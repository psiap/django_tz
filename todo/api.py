from .models import Client, DealsFile
from rest_framework import viewsets, permissions
from .serializers import ClientSerializer, DealsFileSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [
    permissions.AllowAny
    ]
    serializer_class = ClientSerializer

class DealsFileViewSet(viewsets.ModelViewSet):
    queryset = DealsFile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DealsFileSerializer

