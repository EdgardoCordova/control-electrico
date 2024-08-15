from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    batch_crc_PROG_view,
)

app_name = 'programs'

urlpatterns = [
    path('batch_crc_PROG/', batch_crc_PROG_view),
    
]
