from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('comics', views.ComicBookViewSet)

urlpatterns = router.urls
