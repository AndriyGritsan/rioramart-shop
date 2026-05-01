from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import RegisterForm, PasswordResetForm, LoginForm, ProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from shop.models import Order, Wishlist
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
class RegisterUserView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = RegisterForm
    success_url = '/'
    
    
class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    def get_success_url(self):
        return self.request.GET.get('next', '/')
    
    
def user_logout(request):
    logout(request)
    return redirect('/')


@login_required
def account(request):
    page = request.GET.get('page', 'dashboard')
    
    if request.method == "POST" and "profile_submit" in request.POST:
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=request.user)
        
    if request.method == "POST" and "password_submit" in request.POST:
        pass_form = PasswordChangeForm(request.user, request.POST)
        if pass_form.is_valid():
            user = pass_form.save()
            update_session_auth_hash(request, user)
    else:
        pass_form = PasswordChangeForm(request.user)
    
    
    
    order_count = Order.objects.filter(email=request.user.email).count()
    wishlist_count = Wishlist.objects.filter(user=request.user).count()
    recent_orders = Order.objects.filter(email=request.user.email).order_by('id')[:3]
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
    addresses = Order.objects.filter(email=request.user.email).order_by('-id')
    
    context = {
        'page': page,
        'order_count': order_count,
        'wishlist_count': wishlist_count,
        'recent_orders': recent_orders,
        'wishlist_items': wishlist_items,
        'addresses': addresses,
        'form': form,
        'pass_form': pass_form
    }
    
    return render(request, 'accounts/account.html', context=context)


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/forgot-password.html'
    form_class = PasswordResetForm
    success_url = '/accounts/login/' 
    