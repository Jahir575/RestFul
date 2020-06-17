from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from core.views import *

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='Customer')
router.register(r'profession', ProfessionViewSet)
router.register(r'datasheet', DatasheetViewSet)
router.register(r'documents', DocumentsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
