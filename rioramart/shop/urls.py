from django.urls import path
from .views import cart, checkout, shop_single, shop, wishlist, add_to_cart, add_to_wishlist, remove_from_cart

app_name = 'shop'

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('add_to_cart/<slug:slug>/', add_to_cart, name='add_to_cart' ), 
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('shop_single/<slug:slug>/', shop_single, name='shop_single'), 
    path('shop/', shop, name='shop'),
    path('wishlist/', wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist')
]

