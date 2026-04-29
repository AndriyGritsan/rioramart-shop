from django.urls import path
from .views import blog, blog_single

app_name = 'blog'

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog_single/<slug:slug>/', blog_single, name='blog_single')
    
]
 