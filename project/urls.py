from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from product.api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', DestinationViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/accounts/", include("account.urls")),
    path("api/v1/products/", include("product.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
urlpatterns += router.urls