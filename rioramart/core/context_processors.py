from .models import Contact, Subscription
from shop.models import Category

def global_data(request):
    return {
        'menu_categories': Category.objects.all(),
        'contact': Contact.objects.first()
    }
    

