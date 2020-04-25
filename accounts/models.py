from enum import IntEnum

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# fixtureでユーザを作りたい場合は、以下のようにして作る
# https://stackoverflow.com/questions/34321075/how-to-add-superuser-in-django-from-fixture


class PermissionType(models.IntegerChoices):
    ADMIN = (1, 'システム管理者')
    MANAGER = (2, '管理職')
    EMPLOYEE = (3, '一般')


class Section(models.Model):
    name = models.CharField(max_length=100)


# templateで "has_perm" を使うには、Userに "has_perm" メソッドを用意して認証バックエンドに依頼する処理が必要
# https://github.com/dfunckt/django-rules/blob/v2.2.0/rules/templatetags/rules.py#L15
# 今回は PermissionsMixin を使っておく
class User(AbstractBaseUser, PermissionsMixin):
    # AbstractUserよりコピペして、不要なものはコメントアウト
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    # first_name = models.CharField(_('first name'), max_length=30, blank=True)
    # last_name = models.CharField(_('last name'), max_length=150, blank=True)
    # email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    # EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']

    # --------------
    # 追加項目 ここから
    # --------------
    display_name = models.CharField(max_length=100)

    # Django3.0からはIntegerChoicesを使える
    permission_type = models.IntegerField(choices=PermissionType.choices,
                                          default=PermissionType.EMPLOYEE)

    section = models.ForeignKey('accounts.Section', on_delete=models.PROTECT)
    # -- 追加項目 ここまで ---

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

        # abstract=Trueだと、Userクラスとして認識されずにエラーが発生する
        # django.core.exceptions.ImproperlyConfigured: AUTH_USER_MODEL refers to model 'accounts.User' that has not been installed
        # abstract = True

    def clean(self):
        super().clean()
        # self.email = self.__class__.objects.normalize_email(self.email)

    # def get_full_name(self):
    #     """
    #     Return the first_name plus the last_name, with a space in between.
    #     """
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()
    #
    # def get_short_name(self):
    #     """Return the short name for the user."""
    #     return self.first_name
    #
    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this user."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)
