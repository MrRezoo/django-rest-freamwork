from rest_framework import routers
from home.api_views import PersonViewSet

router = routers.DefaultRouter()
router.register('person', PersonViewSet, basename='person')
