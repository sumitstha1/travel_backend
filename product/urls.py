from django.urls import path
from .views import *

urlpatterns = [
    path("", DestinationAPIView.as_view())
]
