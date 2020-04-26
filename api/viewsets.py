from rest_framework import mixins
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rules.contrib.rest_framework import AutoPermissionViewSetMixin

from .serializers import NewsSerializer
from myapp.models import DrfNews


class NewsReadOnlyModelViewSet(AutoPermissionViewSetMixin, ReadOnlyModelViewSet):
    queryset = DrfNews.objects.all()
    serializer_class = NewsSerializer


class NewsRetrieveModelViewSet(AutoPermissionViewSetMixin,
                               mixins.RetrieveModelMixin,
                               GenericViewSet):
    queryset = DrfNews.objects.all()
    serializer_class = NewsSerializer
