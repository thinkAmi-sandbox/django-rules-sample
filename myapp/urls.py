from django.urls import path

from .views import NewsListView, NewsDetailView

app_name = 'myapp'

urlpatterns = [
    path('', NewsListView.as_view(), name='index'),
    path('<int:pk>', NewsDetailView.as_view(), name='detail'),
]
