from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class DestinationAPIView(APIView):
    def get(self, request):
        destination_obj = Destination.objects.prefetch_related("location", "city", "imgSrc").all()
        serializer = DestinationSerializer(destination_obj, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)