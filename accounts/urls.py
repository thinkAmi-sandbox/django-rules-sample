from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    # 手抜きでDjango adminのログイン画面を流用
    # 参考：https://stackoverflow.com/a/50688747
    path('login/',
         LoginView.as_view(template_name='admin/login.html'),
         name='login'),

    # こちらも手抜きでDjango adminのログアウト画面を流用
    path('logout/', LogoutView.as_view(), name='logout'),
]
