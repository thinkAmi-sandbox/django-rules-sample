from django.urls import path, include
from rest_framework import routers

from .viewsets import NewsReadOnlyModelViewSet, NewsRetrieveModelViewSet

router = routers.SimpleRouter()
router.register('news', NewsReadOnlyModelViewSet)
router.register('retrieve', NewsRetrieveModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
