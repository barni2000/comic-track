from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('publishers', views.PublisherViewSet)

urlpatterns = router.urls
