from django.urls import path
from .views import home, about, contact, subscribe

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'), 
    path('contact/', contact, name='contact'),
    path('subscribe/', subscribe, name='subscribe')
    
]

