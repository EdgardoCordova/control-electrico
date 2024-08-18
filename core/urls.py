from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import change_theme


urlpatterns = [
    path('admin/', admin.site.urls),
    path('descriptions/', include('descriptions.urls', namespace='descriptions')),
    path('programs/', include('programs.urls', namespace='programs')),
    path('switch/', change_theme, name='change'),
    path("__reload__/", include("django_browser_reload.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
