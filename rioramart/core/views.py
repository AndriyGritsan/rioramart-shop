from django.shortcuts import render, redirect
from .models import Contact, Banner
from .forms import MessageUserForm, SubscriptionUserForm
from shop.models import Category, Product
from blog.models import Post


# Create your views here.
def home(request):
    deals = Product.objects.filter(available=True)[:4]
    new_products = Product.objects.order_by('-id')[:6]
    categories = Category.objects.all()
    
    recommended = Product.objects.filter(available=True).order_by('?')[:6]
    
    main_banners = Banner.objects.filter(type='main', active=True)[:2]
    side_banners = Banner.objects.filter(type='side', active=True)[:1]
    
    blogs = Post.objects.order_by('-created_at' )[:6]
        
    context = {
        'deals': deals,
        'new_products': new_products,
        'categories': categories,
        'recommended': recommended,
        'main_banners': main_banners,
        'side_banners': side_banners,
        'blogs': blogs
    }
    
    return render(request, 'core/index.html', context=context)



def about(request):
    return render(request, 'core/about.html')


def contact(request):
    if request.method == 'POST':
        form = MessageUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MessageUserForm()
    
    contact = Contact.objects.first()
    
    
    context = {
        'contacts': contact,
        
        'message_form': form
    }
    return render(request, 'core/contact.html', context=context)


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionUserForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))