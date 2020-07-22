from rest_framework import routers
from .api import ClientViewSet

router = routers.DefaultRouter()
router.register('api/todo', ClientViewSet, 'todo')

urlpatterns = router.urls