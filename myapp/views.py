from django.views.generic import ListView, DetailView
from rules.contrib.views import PermissionRequiredMixin

from myapp.models import News


class NewsListView(ListView):
    model = News


class NewsDetailView(PermissionRequiredMixin, DetailView):
    model = News
    permission_required = 'myapp.same_section'
