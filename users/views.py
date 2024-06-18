from random import sample

from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from homework_django.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserPasswordResetForm
from users.models import User
import secrets


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Ссылка для подтверждения - {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))

class UserPasswordResetView(PasswordResetView):
    model = User
    form_class = UserPasswordResetForm
    template_name = 'users/password_reset_form.html'
    success_url = reverse_lazy('users:login')

    def generate_password(self):
        symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'
        return ''.join(sample(symbols, 8))

    def form_valid(self, form):
        if self.request.method == 'POST':
            user_email = self.request.POST.get('email')
            user = User.objects.filter(email=user_email).first()

            new_password = self.generate_password()
            user.set_password(new_password)
            user.save()
            send_mail(
                subject='Новый пароль',
                message=f'Ваш новый пароль - {new_password}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
            return HttpResponseRedirect(reverse('users:login'))
        return super().form_valid(form)










