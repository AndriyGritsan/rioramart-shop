from django.urls import path
from .views import RegisterUserView, LoginUserView, user_logout, account, PasswordResetView



urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('account/', account, name='account'),
    
    #password recovery
    path('password_reset/', PasswordResetView.as_view(), name='password_reset')
]
