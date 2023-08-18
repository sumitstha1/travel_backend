from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Destination)
admin.site.register(DestinationImage)