from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order, Review, Wishlist
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',  'image_tag', 'name')
    
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return "-"
    
    image_tag.short_description = 'Image'
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo_tag' ,'name', 'price', 'brand', 'available', 'stock')
    list_filter = ('price', 'category', 'available')
    search_fields = ('name', )
    list_editable = ('price', 'available', 'stock')
    
    def photo_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" />')
        return "-"
    photo_tag.short_description = 'image'

admin.site.register(Cart)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity')
    list_filter = ('cart', 'product')
    search_fields = ('product_name', )
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'city', 'country')
    list_filter = ('country', 'city')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    
    fieldsets = (
        ('Billing Information',{
            'fields':(
                ('first_name', 'last_name'),
                'emaiд', 'phone', 'company_name', 'company_address', 'billing_address_line1', 'billing_address_line2',
                ('city', 'state'),
                ('zip_code', 'country'),
                )
        }),
        
        ('Shopping information',{
            'fields':(
                ('shopping_first_name', 'shopping_last_name'),
                'shopping_email', 'shopping_phone', 'shopping_company', 'shopping_address', 'shopping_address_line1', 'shopping_address_line2',
                ('shopping_city', 'shopping_state'),
                ('shopping_zip_code', 'shopping_country')
            )
        })
    
    )
    ordering = ('id', )
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at', 'product')
    search_fields = ('name', 'text')
    ordering = ('rating', )
    

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('user__email', 'product_name')
    ordering = ('-created_at', )