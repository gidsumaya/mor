from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('rainfall', views.RainfallView)
router.register('mobile', views.MobileView)
router.register('sms', views.SmsView)


urlpatterns = [
    path('', include(router.urls)),
]
