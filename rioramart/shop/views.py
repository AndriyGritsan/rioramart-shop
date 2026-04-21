from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Order, Review, Cart, CartItem, Wishlist
from .forms import OrderForm
from django.db.models import Avg, Count

# Create your views here.
def cart(request):
    if not request.session.session_key:
        request.session.create()
    
    session_key = request.session.session_key
    
    cart, _ = Cart.objects.get_or_create(session_key=session_key)
    
    items = cart.items.select_related('product')
    
    total = 0
    for item in items:
        item.total = item.product.price * item.quantity
        total += item.total
    
    context = {
        'items': items,
        'total': total
    }
    
    return render(request, 'shop/cart.html', context=context)


def add_to_cart(request, slug):
    product = Product.objects.get(slug=slug)
    quantity = int(request.GET.get('quantity', 1))
    
    if not request.session.session_key:
        request.session.create()
        
    session_key = request.session.session_key
    cart, _ = Cart.objects.get_or_create(session_key=session_key)
    
    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )
    
    if not created:
        item.quantity += quantity
        item.save()
        
    return redirect('cart')

def checkout(request):
    cart = Cart.objects.filter(session_key=request.session.session_key).first()

    cart_items = []
    subtotal = 0

    if cart:
        items = cart.items.select_related('product')

        for item in items:
            price = float(item.product.price)
            quantity = item.quantity
            total_price = price * quantity

            subtotal += total_price

            cart_items.append({
                'name': item.product.name,
                'price': price,
                'quantity': quantity,
                'total': total_price
            })

    delivery = 40
    total = subtotal + delivery

    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save()

            if cart:
                cart.items.all().delete()

            return redirect('home')

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'delivery': delivery,
        'total': total,
        'order_form': form
    }
            
    return render(request, 'shop/checkout.html', context=context)



def shop_single(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == "POST":
        name = request.POST.get('name')
        text = request.POST.get('text')
        rating = int(request.POST.get('rating') or 5)
        
        Review.objects.create(
            product=product,
            name = name,
            text = text,
            rating=rating
        )
        
        return redirect('shop_single', slug=slug)
    
    reviews = Review.objects.filter(product=product)
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    reviews_count = reviews.count()
    total = reviews.count()
    
    five_star = reviews.filter(rating=5).count()
    four_star = reviews.filter(rating=4).count()
    three_star = reviews.filter(rating=3).count()
    two_star = reviews.filter(rating=2).count()
    one_star = reviews.filter(rating=1).count()
    
    five_star_pct = (five_star / total * 100) if total else 0
    four_star_pct = (four_star / total * 100) if total else 0
    three_star_pct = (three_star / total * 100) if total else 0
    two_star_pct = (two_star / total * 100) if total else 0
    one_star_pct = (one_star / total * 100) if total else 0
    
    rating_stats = reviews.values('rating').annotate(count=Count('rating'))

    
    related_products = Product.objects.filter(category=product.category)
    
    context = {
        'product': product,
        'related_products': related_products,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'reviews_count': reviews_count,
        'rating_stats': rating_stats,
        'five_star': five_star,
        'four_star': four_star,
        'thee_star': three_star,
        'two_star': two_star,
        'one_star': one_star,
        'five_star_pct': five_star_pct,
        'four_start_pct': four_star_pct,
        'three_star_pct': three_star_pct,
        'two_star_pct': two_star_pct,
        'one_start_pct': one_star_pct
        
    }
    
    return render(request, 'shop/shop-single.html', context=context)



def shop(request):
    category = Category.objects.all()
    
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    
    else:
        products = Product.objects.all()
    
    context = {
        'products': products,
        'categories': category
    }
    
    return render(request, 'shop/shop.html', context=context)



def wishlist(request):
    wishlist = Wishlist.objects.all()
    context = {
        'wishlist': wishlist,
    }
    return render(request, 'shop/wishlist.html', context=context)


def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )
    
    return redirect(request.META.get('HTTP_REFERER'))