from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('account.urls'), name='profile'),
    path('api/v1/', include('comic.urls'), name='comic'),
    path('api/v1/', include('publisher.urls'), name='publisher'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
