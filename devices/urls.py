from django.urls import path, include
from rest_framework import routers
from devices.views import List
from devices.api.views import WarningDeviceViewSet

router = routers.DefaultRouter()
router.register('devices', WarningDeviceViewSet, basename='devices')

app_name = 'main'

urlpatterns = [
    path('', List.as_view()),
    path('api/', include(router.urls)),


]