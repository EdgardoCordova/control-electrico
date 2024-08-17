from django.urls import path
from .views import (
    batch_crc_PROG_view,
    programs_list_view,
    programs_detail_view,
)

app_name = 'programs'

urlpatterns = [
    path('', programs_list_view, name='main'),
    path('batch_crc_PROG/', batch_crc_PROG_view, name='batch'),
    path('detail/<slug>', programs_detail_view, name='detail'),
    
]
