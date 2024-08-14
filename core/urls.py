from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('descriptions/', include('descriptions.urls', namespace='descriptions')),
    path('programs/', include('programs.urls', namespace='programs')),
]


#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
