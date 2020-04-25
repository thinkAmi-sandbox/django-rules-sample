from django.db import models
from rules.contrib.models import RulesModel


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='タイトル')
    content = models.CharField(max_length=100, verbose_name='内容')
    section = models.ForeignKey('accounts.Section', on_delete=models.PROTECT)
