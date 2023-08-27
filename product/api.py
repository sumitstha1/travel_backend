from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import permissions

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [
        permissions.AllowAny
    ]