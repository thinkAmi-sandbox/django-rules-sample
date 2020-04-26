from django.db import models
from rules.contrib.models import RulesModel

from myapp.rules import can_view


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='タイトル')
    content = models.CharField(max_length=100, verbose_name='内容')
    section = models.ForeignKey('accounts.Section', on_delete=models.PROTECT)


class DrfNews(RulesModel):
    title = models.CharField(max_length=50, verbose_name='タイトル')
    content = models.CharField(max_length=100, verbose_name='内容')
    section = models.ForeignKey('accounts.Section', on_delete=models.PROTECT)

    class Meta:
        rules_permissions = {
            'view': can_view
        }
