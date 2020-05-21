from django.urls import path, include
from . import views
from .views import mobile_upload, MobileView, send_sms, ResView


urlpatterns = [
    path('dashboard/', ResView.as_view(), name='home'),
    path('advisory/', mobile_upload, name='mobile_upload'),
    path('advisory/success', send_sms, name='send_sms'),


]