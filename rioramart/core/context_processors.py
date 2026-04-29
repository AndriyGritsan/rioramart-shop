from .models import Contact
from shop.models import Category, Wishlist, CartItem
from .forms import SubscriptionUserForm


def global_data(request):
    cart_count = 0
    wishlist_count = 0
    
    try:
        if request.user.is_authenticated:
            session_key = request.session.session_key
            
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            
            cart_count = CartItem.objects.filter(
                cart__session_key=session_key
            ).count()
            
            wishlist_count = Wishlist.objects.filter(
                user=request.user
            ).count()
            
            
    except Exception:
        pass

    return {
        'subscription_form': SubscriptionUserForm(),
        'menu_categories': Category.objects.all(),
        'contact': Contact.objects.first(),
        'wishlist_count': wishlist_count,
        'cart_count': cart_count,
    }
    

 
        