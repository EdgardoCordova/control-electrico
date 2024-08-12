from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    descriptions_generation_view,
    descriptions_list_view,
)
app_name = 'descriptions'

urlpatterns = [
    path('', descriptions_generation_view),
    path('list/', descriptions_list_view),
    
]
