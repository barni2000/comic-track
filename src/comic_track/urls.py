from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from account.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('account.urls'), name='profile'),
    path('api/v1/', include('comic.urls'), name='comic'),
    path('api/v1/', include('publisher.urls'), name='publisher'),
    path('api/v1/login/', LoginView.as_view()),
    path('api/v1/logout/', LogoutView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
