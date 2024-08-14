from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    crc_DES_init_view,
    descriptions_list_view,
)
app_name = 'descriptions'

urlpatterns = [
    path('', descriptions_list_view),
    path('crc_DES_init/', crc_DES_init_view),
    
]
