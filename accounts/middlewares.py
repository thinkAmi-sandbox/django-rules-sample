from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 全画面ログイン必須なので、ログインしてなかったらログイン画面へ遷移
        if not request.user.is_authenticated and request.path != reverse('accounts:login'):
            return redirect('accounts:login')
