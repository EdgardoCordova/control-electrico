from django.urls import path
from django.contrib import admin

from .views import (
    batch_crc_DES_view,
    descriptions_list_view,
    
)
app_name = 'descriptions'

urlpatterns = [
    path('', descriptions_list_view, name='main'),
    path('batch_crc_DES/', batch_crc_DES_view,name='batch'),
    
]
