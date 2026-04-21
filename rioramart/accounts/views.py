from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import RegisterForm, PasswordResetForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


# Create your views here.
class RegisterUserView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = RegisterForm
    success_url = '/'
    
    
class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    def get_success_url(self):
        return self.request.GET.get('next', '/')
    
    
def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def account(request):
    return render(request, 'accounts/account.html')


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/forgot-password.html'
    form_class = PasswordResetForm
    