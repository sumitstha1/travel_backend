from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class DestinationAPIView(APIView):

    def get_obj(self, slug):
        try:
            return Destination.objects.prefetch_related("location", "city", "imgSrc").get(slug = slug)
        except Destination.DoesNotExist:
            return None

    def get(self, request, slug=None):

        if slug:
            destination_obj = self.get_obj(slug=slug)
            if not destination_obj:
                return Response({"error": "The Destination with the slug doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
            serializer = DestinationSerializer(destination_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)

        destination_obj = Destination.objects.prefetch_related("location", "city", "imgSrc").all()
        serializer = DestinationSerializer(destination_obj, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)